from __future__ import annotations # Delayed evaluation of type hints (PEP 563)

from websockets.exceptions import ConnectionClosed as WebSocketConnectionClosed
from websockets import connect as websocket_connect, ClientConnection as WebSocketClientConnection
from asyncio import Event, Future, get_running_loop, wait_for, gather, create_task
from typing import Optional, Union, List, Dict, Callable, Coroutine
from enum import Enum
from abc import ABC, abstractmethod
import logging
import json

from resonitelink.models.assets.mesh import \
    Vertex, Submesh, Blendshape, Bone, \
    SubmeshRawData, BlendshapeRawData, BoneWeightRawData
from resonitelink.models.responses import Response, SessionData, SlotData, ComponentData, AssetData
from resonitelink.models.datamodel import \
    Member, Reference, Slot, Component, \
    Float3, Float4, FloatQ, Color, \
    Field_Bool, Field_Long, Field_Float3, Field_FloatQ, Field_String
from resonitelink.models.messages import \
    Message, BinaryPayloadMessage, RequestSessionData, \
    GetSlot, AddSlot, UpdateSlot, RemoveSlot, \
    GetComponent, AddComponent, UpdateComponent, RemoveComponent, \
    ImportAudioClipFile, ImportAudioClipRawData, \
    ImportMeshJSON, ImportMeshRawData, \
    ImportTexture2DFile, ImportTexture2DRawData, ImportTexture2DRawDataHDR

from resonitelink.utils.id_registry import IDRegistry
from resonitelink.exceptions import ResoniteLinkException
from resonitelink.proxies import SlotProxy, ComponentProxy
from resonitelink.utils import get_slot_id, get_component_id, optional_slot_reference, optional_field
from resonitelink.json import MISSING, ResoniteLinkJSONDecoder, ResoniteLinkJSONEncoder, format_object_structure


__all__ = (
    'ResoniteLinkClient',
    'ResoniteLinkWebsocketClient'
)


class _ResoniteLinkClientEvent(Enum):
    """
    All event types that can be subscribed to in a `ResoniteLinkClient`.

    """
    STARTING=0
    STARTED=1
    STOPPING=2
    STOPPED=3
    MESSAGE_SENT=4
    RESPONSE_RECEIVED=5


class ResoniteLinkClient(ABC):
    """
    Abstract base class for all ResoniteLink-Clients.

    """
    _on_starting : Event
    _on_started : Event
    _on_stopping : Event
    _on_stopped : Event
    _event_handlers : Dict[_ResoniteLinkClientEvent, List[Callable[[ResoniteLinkClient], Coroutine]]]
    _message_ids : IDRegistry[Future[Response]]
    _datamodel_ids : IDRegistry

    def __init__(self, logger : Optional[logging.Logger] = None, log_level : int = logging.INFO):
        """
        Base constructur of ResoniteLinkClient instance.

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
        self._message_ids = IDRegistry()
        self._datamodel_ids = IDRegistry()
    
    def _log(self, log_level : int, msg_fn : Callable[..., str], *args, **kwargs):
        """
        Internal log function that doesn't evaluate the msg function when it wouldn't get logged.

        """
        if self._logger.isEnabledFor(log_level):
            self._logger.log(log_level, msg_fn(*args, **kwargs))

    async def stop(self):
        """
        Disconnects this ResoniteLinkClient and stops processing messages. This cannot be undone!
        
        """
        await self._stop()
    
    def on_starting(self, func : Callable[[ResoniteLinkClient], Coroutine]):
        """
        Decorator syntax to register an event handler to the `STARTING` event.

        """
        self._register_event_handler(_ResoniteLinkClientEvent.STARTING, func)
        return func
    
    def on_started(self, func : Callable[[ResoniteLinkClient], Coroutine]):
        """
        Decorator syntax to register an event handler to the `STARTED` event.

        """
        self._register_event_handler(_ResoniteLinkClientEvent.STARTED, func)
        return func
    
    def on_stopping(self, func : Callable[[ResoniteLinkClient], Coroutine]):
        """
        Decorator syntax to register an event handler to the `STOPPING` event.

        """
        self._register_event_handler(_ResoniteLinkClientEvent.STOPPING, func)
        return func
    
    def on_stopped(self, func : Callable[[ResoniteLinkClient], Coroutine]):
        """
        Decorator syntax to register an event handler to the `STOPPED` event.

        """
        self._register_event_handler(_ResoniteLinkClientEvent.STOPPED, func)
        return func

    def on_message_sent(self, func : Callable[[ResoniteLinkClient, Message], Coroutine]):
        """
        Decorator syntax to register an event handler to the `MESSAGE_SENT` event.

        """
        self._register_event_handler(_ResoniteLinkClientEvent.MESSAGE_SENT, func)
        return func

    def on_response_received(self, func : Callable[[ResoniteLinkClient, Response], Coroutine]):
        """
        Decorator syntax to register an event handler to the `RESPONSE_RECEIVED` event.

        """
        self._register_event_handler(_ResoniteLinkClientEvent.RESPONSE_RECEIVED, func)
        return func

    def _register_event_handler(self, event : _ResoniteLinkClientEvent, handler : Callable[..., Coroutine]):
        """
        Registers a new event handler to be invoked when the specified client event occurs.
        This shouldn't be called directly from the outside, as it doesn't use strict typing for the `handler` parameter.

        """
        handlers = self._event_handlers.setdefault(event, [ ])
        handlers.append(handler)
        self._log(logging.DEBUG, lambda: f"Updated event handlers: {self._event_handlers}")
    
    async def _invoke_event_handlers(self, event : _ResoniteLinkClientEvent, *args, **kwargs):
        """
        Invokes all registered event handlers for the given event. 

        """
        handlers = self._event_handlers.setdefault(event, [ ])
        self._log(logging.DEBUG, lambda: f"Invoking {len(handlers)} event handlers for event {event}")
        await gather(*[ handler(self, *args, **kwargs) for handler in handlers ])
    
    async def request_session_data(self) -> SessionData:
        """
        Requests the session data of the current ResoniteLink connection.

        Returns
        -------
        A `SessionData` instance containing the requested data.

        """
        msg = RequestSessionData()
        response = await self.send_message(msg)
        if not isinstance(response, SessionData):
            raise RuntimeError(f"Unexpected response type for message `RequestSessionData`: `{type(response)}` (Expected: `SessionData`)")
        
        return response
    
    async def get_slot(
        self, 
        slot : Union[str, Slot, SlotProxy, Reference], 
        depth : int = 0, 
        include_component_data : bool = False
    ) -> Slot:
        """
        Fetches a slot from ResoniteLink.

        Parameters
        ----------
        slot : Union[str, Slot, SlotProxy, Reference]
            Unique ID or reference of the slot we're requesting data for. 
            Special case: "Root" will fetch the root slot of the world.
        depth : int, default = 0
            How deep to fetch the hierarchy. Value of 0 will fetch only the requested slot fully. 
            Value of 1 will fully fetch the immediate children. Value of -1 will fetch everything fully. 
            Any immediate children of slots beyond this depth will be fetched as references only.
        include_component_data : bool, default = False
            Indicates if components should be fetched fully with all their data or only as references. 
            Set to False if you plan on fetching the individual component data later.
        
        Returns
        -------
        An instance of the `Slot` data class containing the requested data.

        """
        slot_id = get_slot_id(slot)
        msg = GetSlot(
            slot_id = slot_id, 
            depth=depth, 
            include_component_data = include_component_data
        )
        response = await self.send_message(msg)
        if not isinstance(response, SlotData):
            raise RuntimeError(f"Unexpected response type for message `GetSlot`: `{type(response)}` (Expected: `SlotData`)")
        
        return response.data
    
    async def add_slot(
        self,
        parent : Union[str, Slot, SlotProxy, Reference] = Slot.Root, 
        position : Float3 = MISSING,
        rotation : FloatQ = MISSING,
        scale : Float3 = MISSING,
        is_active : bool = MISSING,
        is_persistent : bool = MISSING,
        name : str = MISSING,
        tag : str = MISSING,
        order_offset : int = MISSING
    ) -> SlotProxy:
        """
        Creates a new slot with the provided arguments.

        Parameters
        ----------
        parent : Union[str, Slot, SlotProxy, Reference]
            Unique ID or reference to the parent slot this slot should be added under.
        position : Float3, optional
            Local position of the slot.
        rotation : FloatQ, optional
            Local rotation of the slot.
        scale : Float3, optional
            Local scale of the slot.
        is_active : bool, optional
            Active state of the slot.
        is_persistent : bool, optional
            Persistent state of the slot.
        name : str, optional
            Name of the slot.
        tag : str, optional
            Tag of the slot.
        order_offset : int, optional
            Order offset of the slot.

        Returns
        -------
        Returns a `SlotProxy` instance for the newly created slot.

        """
        slot_id = self._datamodel_ids.generate_id()
        parent_slot_id = get_slot_id(parent)
        self._log(logging.DEBUG, lambda: f"Parent slot: {parent}, parent slot id: {parent_slot_id}")
        msg = AddSlot(data=Slot(
            id = slot_id, 
            parent = Reference(target_id=parent_slot_id, target_type="[FrooxEngine]FrooxEngine.Slot"),
            position = optional_field(position, Field_Float3),
            rotation = optional_field(rotation, Field_FloatQ),
            scale = optional_field(scale, Field_Float3),
            is_active = optional_field(is_active, Field_Bool),
            is_persistent = optional_field(is_persistent, Field_Bool),
            name = optional_field(name, Field_String),
            tag = optional_field(tag, Field_String),
            order_offset = optional_field(order_offset, Field_Long)
        ))
        await self.send_message(msg)
        return SlotProxy(self, slot_id)
    
    async def update_slot(
        self, 
        slot : Union[str, Slot, SlotProxy, Reference],
        parent : Union[str, Slot, SlotProxy, Reference] = MISSING, 
        position : Float3 = MISSING,
        rotation : FloatQ = MISSING,
        scale : Float3 = MISSING,
        is_active : bool = MISSING,
        is_persistent : bool = MISSING,
        name : str = MISSING,
        tag : str = MISSING,
        order_offset : int = MISSING
    ):
        """
        Updates a slot with the provided fields.
        Any field that isn't provided will be left as is.

        Parameters
        ----------
        slot : Union[str, Slot, SlotProxy, Reference]
            Unique ID or reference of the slot to update.
        parent : Union[str, Slot, SlotProxy, Reference], optional
            Unique ID or reference to the parent slot this slot should be added under.
        position : Float3, optional
            Local position of the slot.
        rotation : FloatQ, optional
            Local rotation of the slot.
        scale : Float3, optional
            Local scale of the slot.
        is_active : bool, optional
            Active state of the slot.
        is_persistent : bool, optional
            Persistent state of the slot.
        name : str, optional
            Name of the slot.
        tag : str, optional
            Tag of the slot.
        order_offset : int, optional
            Order offset of the slot.

        """
        slot_id = get_slot_id(slot)
        msg = UpdateSlot(data=Slot(
            id = slot_id, 
            parent = optional_slot_reference(parent),
            position = optional_field(position, Field_Float3),
            rotation = optional_field(rotation, Field_FloatQ),
            scale = optional_field(scale, Field_Float3),
            is_active = optional_field(is_active, Field_Bool),
            is_persistent = optional_field(is_persistent, Field_Bool),
            name = optional_field(name, Field_String),
            tag = optional_field(tag, Field_String),
            order_offset = optional_field(order_offset, Field_Long)
        ))
        await self.send_message(msg)

    async def remove_slot(self, slot : Union[str, Slot, SlotProxy, Reference]):
        """
        Removes a slot.

        Parameters
        ----------
        slot : Union[str, Slot, SlotProxy, Reference]
            Unique ID or reference of the slot to remove.

        """
        slot_id = get_slot_id(slot)
        msg = RemoveSlot(slot_id=slot_id)
        await self.send_message(msg)

    async def get_component(self, component : Union[str, Component, ComponentProxy, Reference]) -> Component:
        """
        Request for full data of a particular component.
        
        Parameters
        ----------
        component : Union[str, Component, ComponentProxy, Reference]
            Unique ID or reference of the component that's being fetched.

        """
        component_id = get_component_id(component)
        msg = GetComponent(component_id=component_id)
        response = await self.send_message(msg)
        if not isinstance(response, ComponentData):
            raise RuntimeError(f"Unexpected response type for message `GetComponent`: `{type(response)}` (Expected: `ComponentData`)")
        
        return response.data

    async def add_component(
        self, 
        container_slot : Union[str, Slot, SlotProxy, Reference],
        component_type : str,
        **members : Member
    ) -> ComponentProxy:
        """
        Creates a new component on a slot.

        Parameters
        ----------
        container_slot : Union[str, Slot, SlotProxy, Reference]
            Unique ID or reference of the slot to attach the new component to.
        component_type : str
            Type of the component to create.
        members : Dict[str, Member], optional
            Members of the component to create. Any field that isn't provided will be populated with the component's default values.

        Returns
        -------
        Returns a `ComponentProxy` instance for the newly created component.
        
        """
        container_slot_id = get_slot_id(container_slot)
        component_id = self._datamodel_ids.generate_id()
        msg = AddComponent(
            container_slot_id=container_slot_id,
            data=Component(
                id=component_id,
                component_type=component_type,
                members=members if members else MISSING
            )
        )
        await self.send_message(msg)
        return ComponentProxy(self, component_id)

    async def update_component(
        self, 
        component : Union[str, Component, ComponentProxy, Reference],
        **members : Member
    ):
        """
        Updates an existng component.

        Parameters
        ----------
        component : Union[str, Component, ComponentProxy, Reference]
            Unique ID or reference of the component to update.
        members : Dict[str, Member]
            Dict of members to update. Any field that isn't provided will be left as is.

        """
        component_id = get_component_id(component)
        msg = UpdateComponent(
            data=Component(
                id=component_id,
                members=members
            )
        )
        await self.send_message(msg)

    async def remove_component(self, component : Union[str, Component, ComponentProxy, Reference]):
        """
        Removes a component.

        Parameters
        ----------
        component : Union[str, Component, ComponentProxy, Reference]
            Unique ID or reference of the component to remove.

        """
        component_id = get_component_id(component)
        msg = RemoveComponent(
            component_id=component_id
        )
        await self.send_message(msg)
    
    async def import_audio_clip_file(self, file_path : str) -> str:
        """
        Imports an audio clip from a file.

        Parameters
        ----------
        file_path : str
            The path to the audio file to import.
        
        Returns
        -------
        Asset URL of the imported audio clip.

        """
        msg = ImportAudioClipFile(file_path=file_path)
        response = await self.send_message(msg)
        if not isinstance(response, AssetData):
            raise RuntimeError(f"Unexpected response type for message `ImportAudioClipFile`: `{type(response)}` (Expected: `AssetData`)")
        
        return response.asset_url

    async def import_audio_clip_raw_data(
        self,
        sample_count : int,
        sample_rate : int,
        channel_count : int,
        samples : List[float]
    ) -> str:
        """
        Imports an audio clip from raw data.

        Parameters
        ----------
        sample_count : int
            Number of audio samples in this audio clip. This does NOT account for channel count and will be the same
            regardless of mono/stereo/5.1 etc.
        sample_rate : int
            Sample rate of the audio data.
        channel_count : int
            Number of audio channels. 1 mono, 2 stereo, 6 is 5.1 surround.
            It's your responsibility to make sure that Resonite supports given audio channel count.
            The actual audio sample data is interleaved in the buffer.
        samples : List[float]
            Raw samples of the audio data.
        
        Returns
        -------
        Asset URL of the imported audio clip.

        """
        msg = ImportAudioClipRawData(
            sample_count=sample_count,
            sample_rate=sample_rate,
            channel_count=channel_count,
            init_samples=samples
        )
        response = await self.send_message(msg)
        if not isinstance(response, AssetData):
            raise RuntimeError(f"Unexpected response type for message `ImportAudioClipRawData`: `{type(response)}` (Expected: `AssetData`)")
        
        return response.asset_url

    async def import_mesh_json(
        self,
        vertices : List[Vertex],
        submeshes : List[Submesh] = MISSING,
        bones : List[Bone] = MISSING,
        blendshapes : List[Blendshape] = MISSING
    ) -> str:
        """
        Imports a mesh from JSON data.
        NOTE: This is mostly provided for completeness. You should generally always use `import_mesh_raw_data`, as it is much more efficient.

        Parameters
        ----------
        vertices : List[Vertex]
            Vertices of this mesh. These are shared across sub-meshes.
        submeshes : List[Submesh], optional
            List of submeshes (points, triangles...) representing this mesh.
            Meshes will typically have at least one submesh.
            Each submesh uses indicies of the vertices for its primitives.
        bones : List[Bone], optional
            Bones of the mesh when data represents a skinned mesh.
            These will be referred to by their index from vertex data.
        blendshapes : List[Blendshape], optional
            Blendshapes of this mesh.
            These allow modifying the vertex positions, normals & tangents for animations such as facial expressions.
        
        Returns
        -------
        Asset URL of the imported mesh.

        """
        msg = ImportMeshJSON(
            vertices=vertices,
            submeshes=submeshes,
            bones=bones,
            blendshapes=blendshapes
        )
        response = await self.send_message(msg)
        if not isinstance(response, AssetData):
            raise RuntimeError(f"Unexpected response type for message `ImportMeshJSON`: `{type(response)}` (Expected: `AssetData`)")
        
        return response.asset_url
    
    async def import_mesh_raw_data(
        self,
        positions : List[Float3],
        normals : Optional[List[Float3]] = None,
        tangents : Optional[List[Float4]] = None,
        colors : Optional[List[Color]] = None,
        uv_channel_dimensions : List[int] = [],
        uvs : Optional[List[List[float]]] = None,
        bone_weights : Optional[List[BoneWeightRawData]] = None,
        submeshes : List[SubmeshRawData] = MISSING,
        blendshapes : List[BlendshapeRawData] = MISSING,
        bones : List[Bone] = MISSING
    ) -> str:
        """
        Imports a mesh from raw data.

        Parameters
        ----------
        positions : List[Float3]
            Positions of the mesh.
        normals : List[Float3], optional
            Vertex normals of the mesh.
        tangents : List[Float4], optional
            Vertex tangents of the mesh.
        colors : List[Color], optional
            Vertex colors of the mesh.
        uv_channel_dimensions : List[int], optional
            Configuration of UV channels for this mesh.
            Each entry represents one UV channel of the mesh.
            Number indicates number of UV dimensions. This must be between 2 and 4 (inclusive).
        uvs : List[List[float]], optional
            UVs of the mesh.
        bone_weights : List[BoneWeightRawData], optional
            How many bone weights does each vertex have.
            If some vertices have fewer bone weights, use weight of 0 for remainder bindings.
        submeshes : List[SubmeshRawData] = MISSING
            Submeshes that form this mesh. Meshes will typically have at least one submesh.
        blendshapes : List[BlendshapeRawData] = MISSING
            Blendshapes of this mesh.
            These allow modifying the vertex positions, normals & tangents for animations such as facial expressions.
        bones : List[Bone] = MISSING
            Bones of the mesh when data represents a skinned mesh.
            These will be referred to by their index from vertex data.
        
        Returns
        -------
        Asset URL of the imported mesh.

        """
        msg = ImportMeshRawData(
            init_positions=positions,
            init_normals=normals,
            init_tangents=tangents,
            init_colors=colors,
            uv_channel_dimensions=uv_channel_dimensions,
            init_uvs=uvs,
            init_bone_weights=bone_weights,
            submeshes=submeshes,
            blendshapes=blendshapes,
            bones=bones
        )
        response = await self.send_message(msg)
        if not isinstance(response, AssetData):
            raise RuntimeError(f"Unexpected response type for message `ImportMeshRawData`: `{type(response)}` (Expected: `AssetData`)")
        
        return response.asset_url
    
    async def import_texture_2d_file(self, file_path : str) -> str:
        """
        Imports a 2D texture from a file.

        Parameters
        ----------
        file_path : str
            The path to the texture file to import.
        
        Returns
        -------
        Asset URL of the imported texture.

        """
        msg = ImportTexture2DFile(file_path=file_path)
        response = await self.send_message(msg)
        if not isinstance(response, AssetData):
            raise RuntimeError(f"Unexpected response type for message `ImportTexture2DFile`: `{type(response)}` (Expected: `AssetData`)")
        
        return response.asset_url
    
    async def import_texture_2d_raw_data(
        self,
        width : int,
        height : int,
        data : List[int],
        color_profile : str = 'sRGB'
    ) -> str:
        """
        Imports a 2D texture from raw data.

        Parameters
        ----------
        width : int
            Width of the texture in pixels.
        height : int
            Height of the texture in pixels.
        data : List[int]
            The pixel data. List of RGBA values between `0` and `255` (`byte`).
            Data must have a length of `width * height * 4`.
        color_profile : str, default = 'sRGB'
            The color profile of the texture data.
        
        Returns
        -------
        Asset URL of the imported texture.

        """
        msg = ImportTexture2DRawData(
            width=width,
            height=height,
            init_data=data,
            color_profile=color_profile
        )
        response = await self.send_message(msg)
        if not isinstance(response, AssetData):
            raise RuntimeError(f"Unexpected response type for message `ImportTexture2DRawData`: `{type(response)}` (Expected: `AssetData`)")
        
        return response.asset_url
    
    async def import_texture_2d_raw_data_hdr(
        self,
        width : int,
        height : int,
        data : List[float]
    ) -> str:
        """
        Imports a 2D texture from raw data.

        Parameters
        ----------
        width : int
            Width of the texture in pixels.
        height : int
            Height of the texture in pixels.
        data : List[float]
            The pixel data. List of RGBA floating point values (`float`).
            Data must have a length of `width * height * 4`.
            Color space is always linear.
        
        Returns
        -------
        Asset URL of the imported texture.

        """
        msg = ImportTexture2DRawDataHDR(
            width=width,
            height=height,
            init_data=data
        )
        response = await self.send_message(msg)
        if not isinstance(response, AssetData):
            raise RuntimeError(f"Unexpected response type for message `ImportTexture2DRawDataHDR`: `{type(response)}` (Expected: `AssetData`)")
        
        return response.asset_url
    
    async def send_message(self, message : Message) -> Response:
        """
        Sends a message to the server.

        """
        # Create an ID for this message and link it to a new future.
        message_future : Future[Response] = get_running_loop().create_future()
        message_id = self._message_ids.generate_id(message_future)
        message.message_id = message_id

        # Encodes the message object and sends it as text.
        raw_message = json.dumps(message, cls=ResoniteLinkJSONEncoder)

        await self._send_raw_message(raw_message, text=True)

        if isinstance(message, BinaryPayloadMessage):
            # The message also has a binary payload that we need to send.
            await self._send_raw_message(message.raw_binary_payload, text=False)
        
        # Log send message
        self._log(logging.INFO, lambda: f"SENT: Resonite ←🗅 {type(message).__name__} (Message-ID: {message_id})")
        
        # Invoke message sent event BEFORE waiting for message's future
        await self._invoke_event_handlers(_ResoniteLinkClientEvent.MESSAGE_SENT, message)
        
        # Waits for the message's future. Will complete when the response is received, of abort after timeout.
        return await wait_for(message_future, timeout=60)
    
    async def _process_message(self, message_bytes : bytes):
        """
        Called when a message was received via the connected websocket.
        
        Parameters
        ----------
        message : bytes
            The received message to process

        """
        self._log(logging.DEBUG, lambda: f"Received raw message: {message_bytes.decode('utf-8')}")
        
        # Decode message into object
        response : Response = json.loads(message_bytes, cls=ResoniteLinkJSONDecoder, root_model_type=Response)
        
        self._log(logging.DEBUG, lambda: f"Response data:\n   {'\n   '.join(format_object_structure(response, print_missing=True).split('\n'))}")

        # We're only expecting responses that we sent, so they should always have a `source_message_id`!
        if not response.source_message_id:
            raise RuntimeError(f"Received response did not include a `source_message_id`!")

        self._log(logging.INFO, lambda: f"RECV: Resonite 🗅→ {type(response).__name__} (Message-ID: {response.source_message_id})")

        try:
            source_message_future = self._message_ids.pop_id_value(response.source_message_id)
        except KeyError:
            # ID unknown or ID value already requested
            raise RuntimeError(f"Received response's `source_message_id` could not get resolved to source message's future!")

        # Invoke message sent event BEFORE responding to message's future
        await self._invoke_event_handlers(_ResoniteLinkClientEvent.RESPONSE_RECEIVED, response)

        # Responds to the future, this will continue the original message sent
        if response.success:
            source_message_future.set_result(response)
        else:
            source_message_future.set_exception(ResoniteLinkException(response))

    @abstractmethod
    async def _stop(self):
        """
        Disconnects this ResoniteLinkClient and stops processing messages.
        Needs to be implemented by implementation.
        
        """
        raise NotImplementedError()

    @abstractmethod
    async def _send_raw_message(self, message : Union[bytes, str], text : bool = True):
        """
        Send a raw message (bytes or str) to the server.
        Needs to be implemented by implementation.

        """
        raise NotImplementedError()


class ResoniteLinkWebsocketClient(ResoniteLinkClient):
    """
    Client to connect to the ResoniteLink API via WebSocket.

    """
    _ws_uri : str
    _ws : WebSocketClientConnection

    def __init__(self, logger : Optional[logging.Logger] = None, log_level : int = logging.INFO):
        """
        Creates a new ResoniteLinkWebsocketClient instance.

        Parameters
        ----------
        logger : Logger, optional
            If provided, this logger will be used instead of the default 'ResoniteLinkClient' logger.
        log_level : int, default = logging.INFO
            The log level to use for the default 'ResoniteLinkClient'. Only has an effect if no override logger is provided.

        """
        super().__init__(logger=logger, log_level=log_level)
    
    async def start(self, port : int = -1, auto_discover : bool = False):
        """
        Connects this ResoniteLinkClient to the ResoniteLink API and starts processing messages.

        Parameters
        ----------
        port : int, default = -1
            The port number to connect to.
        auto_discover : bool, default = True
            If set, the client will automatically connect to the port of the first ResoniteLink session it discovers on the local network.
            This option will override any manually specified port number.

        """
        if self._on_stopped.is_set(): 
            raise Exception("Cannot re-start a client that was already stopped!")
        if self._on_starting.is_set(): 
            raise Exception("Client is already starting!")
        if (port <= 0 and not auto_discover):
            raise ValueError(f"Either a port number must be specified, or auto discovery must be enabled.")
        
        if auto_discover:
            # Connect to first discovered ResoniteLink session on local network
            from resonitelink.utils.session_listener import ResoniteLinkSessionListener
            
            session_listener = ResoniteLinkSessionListener()
            async with session_listener:
                self._log(logging.INFO, lambda: f"Auto-discovery is enabled, waiting to discover ResoniteLink session...")
                session = await session_listener.get_first_discovered_session()
                self._log(logging.INFO, lambda: f"Discovered ResoniteLink session: '{session.session_name}' (ID: '{session.session_id}') on port {session.link_port}")
                port = session.link_port

        if type(port) is not int:
            raise TypeError(f"Port expected to be of type int, not {type(port)}!")
        
        self._log(logging.INFO, lambda: f"Starting client on port {port}...")
        self._on_starting.set()
        await self._invoke_event_handlers(_ResoniteLinkClientEvent.STARTING)

        # Create the task that starts fetching for websocket messages once the websocket client connects
        create_task(self._fetch_loop())
        
        # Connects the websocket client to the specified port
        self._ws_uri : str = f"ws://localhost:{port}/"
        self._ws = await websocket_connect(self._ws_uri)

        self._log(logging.INFO, lambda: f"Connection established! Connected to ResoniteLink on {self._ws_uri}")
        self._on_started.set()
        await self._invoke_event_handlers(_ResoniteLinkClientEvent.STARTED)

        # Run forever until client is stopped
        await self._on_stopped.wait()

    async def _stop(self):
        """
        Disconnects this ResoniteLinkClient and stops processing messages. This cannot be undone!
        
        """
        self._log(logging.DEBUG, lambda: f"Stopping client...")
        self._on_stopping.set()
        await self._invoke_event_handlers(_ResoniteLinkClientEvent.STOPPING)

        await self._ws.close()

        self._log(logging.DEBUG, lambda: f"Client stopped!")
        self._on_stopped.set()
        await self._invoke_event_handlers(_ResoniteLinkClientEvent.STOPPED)
    
    async def _fetch_loop(self):
        """
        Starts fetching and processing websocket messages.
        This will keep running until the _on_stop event is set!

        """
        await self._on_started.wait() # Wait for client to fully start before fetching messages

        self._log(logging.INFO, lambda: f"Listening to messages...")
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
        
        self._log(logging.INFO, lambda: f"Stopped listening to messages.")

    async def _send_raw_message(self, message : Union[bytes, str], text : bool = True):
        """
        Send a raw message (bytes or str) to the server.

        """
        await self._on_started.wait() # Wait for client to fully start before sending messages

        if not text and (isinstance(message, bytes) or isinstance(message, bytearray)):
            self._log(logging.DEBUG, lambda: f"Sending non-text message with {len(message)} bytes.")
        else:
            self._log(logging.DEBUG, lambda: f"Sending text message: {message}")
        
        await self._ws.send(message, text=text)
