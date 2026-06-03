from __future__ import annotations # Delayed evaluation of type hints (PEP 563)

from threading import Lock
from datetime import timedelta, datetime, timezone
from asyncio import DatagramProtocol, DatagramTransport, Event, Queue, Task, get_running_loop, gather, create_task, sleep
from socket import socket, SO_REUSEADDR, SOCK_DGRAM, AF_INET, SOL_SOCKET
from typing import Final, ReadOnly, Dict, List, Callable, Coroutine, Optional
from enum import Enum
import logging
import json

from resonitelink.models.resonite_link_session import ResoniteLinkSession
from resonitelink.json import ResoniteLinkJSONDecoder


__all__ = (
    'ResoniteLinkSessionListener',
)


ANNOUNCE_PORT : Final[int] = 12512
ANNOUNCE_INTERVAL : Final[timedelta] = timedelta(seconds=10)


class _ResoniteLinkSessionListenerEvent(Enum):
    """
    All event types that can be subscribed to in a `SessionListener`.

    """
    SESSION_DISCOVERED = 0
    SESSION_UPDATED = 1
    SESSION_CLOSED = 2


class _SessionEventData():
    """
    Represents the data of a session event, which is handled in a queue.

    """
    _event : _ResoniteLinkSessionListenerEvent
    _session : ResoniteLinkSession

    @property
    def event(self) -> _ResoniteLinkSessionListenerEvent:
        return self._event
    
    @property
    def session(self) -> ResoniteLinkSession:
        return self._session

    def __init__(self, event : _ResoniteLinkSessionListenerEvent, session : ResoniteLinkSession):
        self._event = event
        self._session = session


class _ResoniteLinkSessionListenerProtocol(DatagramProtocol):
    """
    Protocol for handling ResoniteLink session announcements.

    """
    _listener : ResoniteLinkSessionListener

    def __init__(self, listener : ResoniteLinkSessionListener):
        super().__init__()
        self._listener = listener

    def datagram_received(self, data, addr):
        """
        Called when some datagram is received.
        
        """
        self._listener._log(logging.DEBUG, lambda: f"Received UDP message: {data} from {addr}.")
        session : ResoniteLinkSession
        try:
            session = json.loads(data, cls=ResoniteLinkJSONDecoder, root_model_type=ResoniteLinkSession)
        
        except Exception as ex:
            # Failed to parse session JSON. This most likely indicates malformed data or a different format then expected.
            # In this case, we just ignore it and skip processing it. Could be a different application broadcasting on the ResoniteLink port.
            self._listener._log(logging.DEBUG, lambda: f"Exception decoding UDP message: {ex}")
            return

        if not session.session_id:
            return

        with self._listener._sessions_lock:
            session.last_updated = datetime.now(tz=timezone.utc)

            if session.link_port == 0:
                # This indicates that the session was closed.
                if self._listener._sessions.pop(session.session_id, None):
                    self._listener._session_event_queue.put_nowait(_SessionEventData(_ResoniteLinkSessionListenerEvent.SESSION_CLOSED, session))
                
                return

            if session.session_id in self._listener._sessions.keys():
                # Session already in dict
                self._listener._sessions[session.session_id] = session
                self._listener._session_event_queue.put_nowait(_SessionEventData(_ResoniteLinkSessionListenerEvent.SESSION_UPDATED, session))
            
            else:
                # Session not yet in dict
                self._listener._sessions[session.session_id] = session
                self._listener._session_event_queue.put_nowait(_SessionEventData(_ResoniteLinkSessionListenerEvent.SESSION_DISCOVERED, session))
                    
    def error_received(self, exc):
        """
        Called when a send or receive operation raises an OSError.
        (Other than BlockingIOError or InterruptedError.)
        
        """
        print(f"Received error: {exc}")


class ResoniteLinkSessionListener():
    """
    Helper class to discover ResoniteLink sessions currently running on the local network.

    """
    _event_handlers : Dict[_ResoniteLinkSessionListenerEvent, List[Callable[[ResoniteLinkSessionListener, ResoniteLinkSession], Coroutine]]]
    _session_event_queue : Queue[_SessionEventData]
    _first_discovered_session : Optional[ResoniteLinkSession]
    _sessions : Dict[str, ResoniteLinkSession]
    _sessions_lock : Lock
    _transport : DatagramTransport
    _protocol : _ResoniteLinkSessionListenerProtocol
    _expire_sessions_task : Task
    _event_queue_task : Task
    _on_starting : Event
    _on_started : Event
    _on_stopping : Event
    _on_stopped : Event
    _on_first_session_discovered : Event

    @property
    def sessions(self) -> Dict[str, ResoniteLinkSession]:
        """
        Returns a copy of the currently discovered sessions dictionary.
        (The dict is copied to prevent outside modification).

        """
        return self._sessions.copy()

    def __init__(self, logger : Optional[logging.Logger] = None, log_level : int = logging.INFO):
        """
        Base constructur of SessionListener instance.

        Parameters
        ----------
        logger : Logger, optional
            If provided, this logger will be used instead of the default 'SessionListener' logger.
        log_level : int, default = logging.INFO
            The log level to use for the default 'SessionListener'. Only has an effect if no override logger is provided.

        """
        if logger:
            self._logger = logger
        else:
            self._logger = logging.getLogger("SessionListener")
            self._logger.setLevel(log_level)
        self._event_handlers = {}
        self._session_event_queue = Queue(-1)
        self._first_discovered_session = None
        self._sessions = {}
        self._sessions_lock = Lock()
        self._on_starting = Event()
        self._on_started = Event()
        self._on_stopping = Event()
        self._on_stopped = Event()
        self._on_first_session_discovered = Event()

        @self.on_session_discovered
        async def _on_session_discovered(listener, session : ResoniteLinkSession):
            """
            The first discovered session is separately remembered and triggers an event.
            This is used for the `get_first_session()` method.

            """
            if self._on_first_session_discovered.is_set():
                return

            self._first_discovered_session = session
            self._on_first_session_discovered.set()
    
    async def __aenter__(self):
        await self.start()
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.stop()
    
    def on_session_discovered(self, func : Callable[[ResoniteLinkSessionListener, ResoniteLinkSession], Coroutine]):
        """
        Decorator syntax to register an event handler to the `SESSION_DISCOVERED` event.

        """
        self._register_event_handler(_ResoniteLinkSessionListenerEvent.SESSION_DISCOVERED, func)
        return func
    
    def on_session_updated(self, func : Callable[[ResoniteLinkSessionListener, ResoniteLinkSession], Coroutine]):
        """
        Decorator syntax to register an event handler to the `SESSION_UPDATED` event.

        """
        self._register_event_handler(_ResoniteLinkSessionListenerEvent.SESSION_UPDATED, func)
        return func
    
    def on_session_removed(self, func : Callable[[ResoniteLinkSessionListener, ResoniteLinkSession], Coroutine]):
        """
        Decorator syntax to register an event handler to the `SESSION_CLOSED` event.

        """
        self._register_event_handler(_ResoniteLinkSessionListenerEvent.SESSION_CLOSED, func)
        return func
    
    async def start(self):
        """
        Starts the SessionListener and begins listening for ResoniteLink sessions.

        """
        if self._on_starting.is_set():
            raise ValueError("The SessionListener was already started!")

        self._log(logging.DEBUG, lambda: f"Starting ResoniteLink session listener.")
        self._on_starting.set()

        self._event_queue_task = create_task(self._event_queue_loop())
        self._expire_sessions_task = create_task(self._expire_sessions_loop())
        await self._start_udp_listener()

        self._on_started.set()
    
    async def stop(self):
        """
        Stops the SessionListener.

        """
        if self._on_stopping.is_set():
            raise ValueError("The SessionListener was already stopped!")
        if not self._on_starting.is_set():
            raise ValueError("The SessionListener was not yet started!")

        await self._on_started.wait() # Make sure the listener is fully started before attempting to stop it.

        self._log(logging.DEBUG, lambda: f"Stopping ResoniteLink session listener.")
        self._on_stopping.set()

        self._stop_udp_listener()
        self._expire_sessions_task.cancel() # Cancelling will cause all remaining sessions to be cancelled automatically.
        self._event_queue_task.cancel() # Cancelling will spawn a new task that processes the remaining events in the queue.

        await self._on_stopped.wait() # The _on_stopped event is called after all remaining events in the queue are processed.
    
    async def get_first_discovered_session(self) -> ResoniteLinkSession:
        """
        Retrieves the first discovered ResoniteLink session.

        Note
        ----
        This will return the **FIRST** ResoniteLink session discovered by the listener. If there are currently multiple ResoniteLink sessions running,
        which one it returns is undefined! This is used for a convenience auto-discovery mechanism, however, user facing implementations
        should not make use of this, and instead provide a UI showing all discovered sessions for the user to pick one.

        """
        if not self._on_starting.is_set():
            raise ValueError("The SessionListener was not yet started!")
        if self._on_stopping.is_set():
            raise ValueError("The SessionListener was already stopped!")

        self._log(logging.DEBUG, lambda: "Waiting to discover ResoniteLink session...")
        await self._on_first_session_discovered.wait()
        
        if self._first_discovered_session is None:
            raise ValueError("The _first_discovered_session variable was never set!")
        
        session = self._first_discovered_session
        self._log(logging.DEBUG, lambda: f"Discovered ResoniteLink session: '{session.session_name}' (ID: '{session.session_id}') on port {session.link_port}")
        return session
    
    def _log(self, log_level : int, msg_fn : Callable[..., str], *args, **kwargs):
        """
        Internal log function that doesn't evaluate the msg function when it wouldn't get logged.

        """
        if self._logger.isEnabledFor(log_level):
            self._logger.log(log_level, msg_fn(*args, **kwargs))
    
    def _register_event_handler(self, event : _ResoniteLinkSessionListenerEvent, handler : Callable[..., Coroutine]):
        """
        Registers a new event handler to be invoked when the specified client event occurs.
        This shouldn't be called directly from the outside, as it doesn't use strict typing for the `handler` parameter.

        """
        handlers = self._event_handlers.setdefault(event, [ ])
        handlers.append(handler)
        self._log(logging.DEBUG, lambda: f"Updated event handlers: {self._event_handlers}")
    
    async def _invoke_event_handlers(self, event : _ResoniteLinkSessionListenerEvent, *args, **kwargs):
        """
        Invokes all registered event handlers for the given event. 

        """
        handlers = self._event_handlers.setdefault(event, [ ])
        self._log(logging.DEBUG, lambda: f"Invoking {len(handlers)} event handlers for event {event}")
        if not handlers: return
        await gather(*[ handler(self, *args, **kwargs) for handler in handlers ])
    
    async def _event_queue_loop(self):
        """
        Processes the queue for session events.
        Session events are added to this queue when sessions get discovered / updated / closed & processed asyncronously. 

        """
        try:
            while True:
                event_data = await self._session_event_queue.get()
                await self._invoke_event_handlers(event_data.event, event_data.session)
        
        finally:
            self._log(logging.DEBUG, lambda: f"Stopped processing event queue.")
            create_task(self._flush_event_queue()) # Flushing in new task so this one finishes syncronously
    
    async def _flush_event_queue(self):
        """
        Processes the remaining items in the event queue until it is empty.
        This is used as a cleanup after the event queue loop has finished.
        
        Once the event queue is cleared, the _on_stopped event is triggered.

        """
        self._log(logging.DEBUG, lambda: f"Processing remaining events in queue.")
        while not self._session_event_queue.empty():
            event_data = self._session_event_queue.get_nowait()
            await self._invoke_event_handlers(event_data.event, event_data.session)
        
        self._on_stopped.set()

    async def _expire_sessions_loop(self):
        """
        Periodically checks to ensure expired sessions are considered closed & removed from the sessions list.

        """
        try:
            while True:
                await sleep(ANNOUNCE_INTERVAL.total_seconds())
                self._expire_sessions()
        
        finally:
            self._log(logging.DEBUG, lambda: f"Stopped processing sessions.")
            self._expire_all_sessions() # Instantly expire all remaining sessions.
    
    def _expire_sessions(self):
        """
        Checks all currently known sessions for wether or not they have expired.
        Expired sessions trigger are considered closed & will be removed from the sessions list.

        """
        with self._sessions_lock:
            expired_keys : Optional[List[str]] = None
            for session in self._sessions.values():
                if (session.is_expired(ANNOUNCE_INTERVAL.total_seconds() * 2.5)):
                    self._session_event_queue.put_nowait(_SessionEventData(_ResoniteLinkSessionListenerEvent.SESSION_CLOSED, session))
                    
                    if not expired_keys:
                        expired_keys = []
                    
                    expired_keys.append(session.session_id)
            
            if expired_keys:
                for key in expired_keys:
                    del self._sessions[key]
    
    def _expire_all_sessions(self):
        """
        Expires all currently known sessions. This is called when the SessionListener is stopped.

        """
        self._log(logging.DEBUG, lambda: f"Expiring all remaining sessions.")
        with self._sessions_lock:
            all_sessions = list(self._sessions.values())
            for session in all_sessions:
                self._session_event_queue.put_nowait(_SessionEventData(_ResoniteLinkSessionListenerEvent.SESSION_CLOSED, session))
                del self._sessions[session.session_id]
    
    async def _start_udp_listener(self):
        """
        Creates a UDP socket listening on all addresses on the ResoniteLink announcement port.
        A 'SessionListenerProtocol' instance is created to handle received announcements.

        """
        sock = socket(
            AF_INET, # Address family: Internet 
            SOCK_DGRAM # UDP
        )
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", ANNOUNCE_PORT))

        self._transport, self._protocol = await get_running_loop().create_datagram_endpoint(
            lambda: _ResoniteLinkSessionListenerProtocol(self), 
            sock=sock
        )
    
    def _stop_udp_listener(self):
        """
        Closes the UDP transport (and its owned socket).

        """
        self._transport.abort()
