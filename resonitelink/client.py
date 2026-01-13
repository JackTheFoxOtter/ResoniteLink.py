from __future__ import annotations # Delayed evaluation of type hints (PEP 563)

from resonitelink.models.responses import Response
from resonitelink.models.messages import Message, BinaryPayloadMessage
from websockets.exceptions import ConnectionClosed as WebSocketConnectionClosed
from resonitelink.utils import IDRegistry
from resonitelink.json import ResoniteLinkJSONDecoder, ResoniteLinkJSONEncoder, format_object_structure
from websockets import connect as websocket_connect, ClientConnection as WebSocketClientConnection
from asyncio import AbstractEventLoop, Event, Future, get_running_loop, wait_for, gather
from typing import Optional, Union, List, Dict, Callable, Coroutine, Any
from enum import Enum
import logging
import json


class ResoniteLinkClientEvent(Enum):
    STARTING=0
    STARTED=1
    STOPPING=2
    STOPPED=3
    MESSAGE_SENT=4
    MESSAGE_RECEIVED=5


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
    _message_ids : IDRegistry[Future[Response]]
    _loop : AbstractEventLoop
    _ws_uri : str
    _ws : WebSocketClientConnection

    def __init__(self, logger : Optional[logging.Logger] = None, log_level : int = logging.INFO):
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
        self._message_ids = IDRegistry()
        self._event_handlers = { }

    def register_event_handler(self, event : ResoniteLinkClientEvent, handler : Callable[[ResoniteLinkClient], Coroutine]):
        """
        Registers a new event handler to be invoked when the specified client event occurs.

        """
        handlers = self._event_handlers.setdefault(event, [ ])
        handlers.append(handler)
        
        self._logger.debug(f"Updated event handlers: {self._event_handlers}")
    
    async def _invoke_event_handlers(self, event : ResoniteLinkClientEvent, *args, **kwargs):
        """
        Invokes all registered event handlers for the given event. 

        """
        handlers = self._event_handlers.setdefault(event, [ ])

        self._logger.debug(f"Invoking {len(handlers)} event handlers for event {event}")

        await gather(*[ handler(self, *args, **kwargs) for handler in handlers ])
    
    async def start(self, port : int):
        """
        Connects this ResoniteLinkClient to the ResoniteLink API and starts processing messages.

        Parameters
        ----------
        port : int
            The port number to connect to.

        """
        if type(port) is not int: 
            raise AttributeError(f"Port expected to be of type int, not {type(port)}!")
        if self._on_stopped.is_set(): 
            raise Exception("Cannot re-start a client that was already stopped!")
        if self._on_starting.is_set(): 
            raise Exception("Client is already starting!")
        
        # Get the currently running loop. This will raise a RuntimeError if there is none.
        self._loop = get_running_loop()

        self._logger.debug(f"Starting client on port {port}...")
        self._on_starting.set()
        await self._invoke_event_handlers(ResoniteLinkClientEvent.STARTING)

        # Create the task that starts fetching for websocket messages once the websocket client connects
        self._loop.create_task(self._fetch_loop())
        
        # Connects the websocket client to the specified port
        self._ws_uri : str = f"ws://localhost:{port}/"
        self._ws = await websocket_connect(self._ws_uri)

        self._logger.info(f"Connection established! Connected to ResoniteLink on {self._ws_uri}")
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
        self._logger.debug(f"Received raw message: {message_bytes.decode('utf-8')}")
        
        # Decode message into object
        message : Any = json.loads(message_bytes, cls=ResoniteLinkJSONDecoder)
        self._logger.debug(f"Received message:\n   {'\n   '.join(format_object_structure(message, print_missing=True).split('\n'))}")
        
        # Currently nothing other than `Response` instances and derivatives thereof are expected to be received from ResoniteLink.
        if not isinstance(message, Response):
            raise RuntimeError("Received message did not decode into `Response` instance!")
        response = message

        # We're only expecting responses that we sent, so they should always have a `source_message_id`!
        if not response.source_message_id:
            raise RuntimeError(f"Received response did not include a `source_message_id`!")

        try:
            source_message_future = self._message_ids.pop_id_value(response.source_message_id)
        except KeyError:
            # ID unknown or ID value already requested
            raise RuntimeError(f"Received response's `source_message_id` could not get resolved to source message's future!")

        # Invoke message sent event BEFORE responding to message's future
        await self._invoke_event_handlers(ResoniteLinkClientEvent.MESSAGE_RECEIVED, message)

        # Responds to the future, this will continue the original message sent
        if response.success:
            source_message_future.set_result(response)
        else:
            source_message_future.set_exception(RuntimeError(response.error_info)) # TODO: Custom exception

    async def _send_raw_message(self, message : Union[bytes, str], text : bool = True):
        """
        Send a raw message (bytes or str) to the server.

        """
        await self._on_started.wait() # Wait for client to fully start before sending messages

        if not text and isinstance(message, bytes):
            self._logger.debug(f"Sending non-text message with {len(message)} bytes.")
        else:
            self._logger.debug(f"Sending text message: {message}")
        
        await self._ws.send(message, text=text)
    
    async def send_message(self, message : Message) -> Response:
        """
        Sends a message to the server.

        """
        # Create an ID for this message and link it to a new future.
        message_future : Future[Response] = self._loop.create_future()
        message_id = self._message_ids.generate_id(message_future)
        message.message_id = message_id

        # Encodes the message object and sends it as text.
        raw_message = json.dumps(message, cls=ResoniteLinkJSONEncoder)
        await self._send_raw_message(raw_message, text=True)

        if isinstance(message, BinaryPayloadMessage):
            # The message also has a binary payload that we need to send.
            await self._send_raw_message(message.raw_binary_payload, text=False)
        
        # Invoke message sent event BEFORE waiting for message's future
        await self._invoke_event_handlers(ResoniteLinkClientEvent.MESSAGE_SENT, message)
        
        # Waits for the message's future. Will complete when the response is received, of abort after timeout.
        return await wait_for(message_future, timeout=60)
