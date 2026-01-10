from __future__ import annotations # Delayed evaluation of type hints (PEP 563)

from resonitelink.models.messages import BaseMessage
from resonitelink.json import ResoniteLinkJSONDecoder, ResoniteLinkJSONEncoder
from typing import Union, Dict, List, Callable, Coroutine
from enum import Enum
import json
from asyncio import \
    Event, \
    get_running_loop, \
    gather
from websockets import \
    connect as websocket_connect, \
    ClientConnection as WebSocketClientConnection
from websockets.exceptions import \
    ConnectionClosed as WebSocketConnectionClosed
import logging
import json


class ResoniteLinkClientEvent(Enum):
    STARTING=0
    STARTED=1
    STOPPING=2
    STOPPED=3


class ResoniteLinkClient():
    """
    Client to connect to the ResoniteLink API via WebSocket.

    """
    _logger : logging.Logger
    _on_starting : Event
    _on_started : Event
    _on_stopping : Event
    _on_stopped : Event
    _event_handlers : Dict[ResoniteLinkClientEvent, List[Callable[[ResoniteLinkClient], Coroutine]]]
    _ws_uri : str
    _ws : WebSocketClientConnection

    def __init__(self, logger : Union[logging.Logger, None] = None, log_level : int = logging.INFO):
        """
        Creates a new ResoniteLinkClient instance.

        Parameters
        ----------
        logger : Logger, optional
            If provided, this logger will be used instead of the default 'ResoniteLinkClient' logger.
        log_level : int, default = logging.INFO
            The log level to use for the default 'ResoniteLinkClient'. Only has an effect if no override logger is provided.

        """
        if logger:
            self._logger = logger
        else:
            self._logger = logging.getLogger("ResoniteLinkClient")
            self._logger.setLevel(log_level)
        self._on_starting = Event()
        self._on_started = Event()
        self._on_stopping = Event()
        self._on_stopped = Event()
        self._event_handlers = { }

    def register_event_handler(self, event : ResoniteLinkClientEvent, handler : Callable[[ResoniteLinkClient], Coroutine]):
        """
        Registers a new event handler to be invoked when the specified client event occurs.

        """
        handlers = self._event_handlers.setdefault(event, [ ])
        handlers.append(handler)
        
        self._logger.debug(f"Updated event handlers: {self._event_handlers}")
    
    async def _invoke_event_handlers(self, event : ResoniteLinkClientEvent):
        """
        Invokes all registered event handlers for the given event. 

        """
        handlers = self._event_handlers.setdefault(event, [ ])

        self._logger.debug(f"Invoking {len(handlers)} event handlers for event {event}")

        await gather(*[ handler(self) for handler in handlers ])
    
    async def start(self, port : int):
        """
        Connects this ResoniteLinkClient to the ResoniteLink API and starts processing messages.

        Parameters
        ----------
        port : int
            The port number to connect to.

        """
        if type(port) is not int: raise AttributeError(f"Port expected to be of type int, not {type(port)}!")
        if self._on_stopped.is_set(): raise Exception("Cannot re-start a client that was already stopped!")
        if self._on_starting.is_set(): raise Exception("Client is already starting!")

        self._logger.debug(f"Starting client on port {port}...")
        self._on_starting.set()
        await self._invoke_event_handlers(ResoniteLinkClientEvent.STARTING)

        # Create the task that starts fetching for websocket messages once the websocket client connects
        loop = get_running_loop()
        loop.create_task(self._fetch_loop())
        
        # Connects the websocket client to the specified port
        self._ws_uri : str = f"ws://localhost:{port}/"
        self._ws = await websocket_connect(self._ws_uri)

        self._logger.info(f"Client started!")
        self._on_started.set()
        await self._invoke_event_handlers(ResoniteLinkClientEvent.STARTED)

        # Run forever until client is stopped
        await self._on_stopped.wait()

    async def stop(self):
        """
        Disconnects this ResoniteLinkClient and stops processing messages. This cannot be undone!
        
        """
        self._logger.debug(f"Stopping client...")
        self._on_stopping.set()
        await self._invoke_event_handlers(ResoniteLinkClientEvent.STOPPING)

        await self._ws.close()

        self._logger.debug(f"Client stopped!")
        self._on_stopped.set()
        await self._invoke_event_handlers(ResoniteLinkClientEvent.STOPPED)
    
    async def _fetch_loop(self):
        """
        Starts fetching and processing websocket messages.
        This will keep running until the _on_stop event is set!

        """
        await self._on_started.wait() # Wait for client to fully start before fetching messages

        self._logger.info(f"Listening to messages...")
        while True:
            if self._on_stopped.is_set():
                # Client has been stopped since last run, end fetch loop.
                break
            
            try:
                # Fetches the next message as bytes sting
                message_bytes : bytes = await self._ws.recv(decode=False)
                await self._process_message(message_bytes)
            
            except WebSocketConnectionClosed as ex:
                # TODO: Proper reconnection logic on ConnectionClosed
                self._on_stopped.set()
        
        self._logger.info(f"Stopped listening to messages.")
    
    async def _process_message(self, message_bytes : bytes):
        """
        Called when a message was received via the connected websocket.
        
        Parameters
        ----------
        message : bytes
            The received message to process

        """
        message = json.loads(message_bytes, cls=ResoniteLinkJSONDecoder)
        self._logger.debug(f"Received message: {message}")

    async def _send_raw_message(self, message : Union[bytes, str]):
        """
        Send a raw message (bytes or str) to the server.

        """
        await self._on_started.wait() # Wait for client to fully start before sending messages

        self._logger.debug(f"Sending message: {message}")
        await self._ws.send(message, text=True)
    
    async def send_message(self, message : BaseMessage):
        """
        Sends a message to the server.

        """
        raw_message = json.dumps(message, cls=ResoniteLinkJSONEncoder)
        await self._send_raw_message(raw_message)
