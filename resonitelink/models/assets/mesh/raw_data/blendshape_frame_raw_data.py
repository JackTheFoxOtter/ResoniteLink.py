from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from resonitelink.models.assets.mesh.raw_data import BlendshapeRawData
    from resonitelink.models.datamodel import Float3
    from resonitelink.models.messages import ImportMeshRawData

from dataclasses import InitVar, field
from typing import Optional, List
from array import array

from resonitelink.utils.vector_tools import unpack_vectors_float3, pack_vectors_float3
from resonitelink.json import MISSING, json_model, json_element


__all__ = (
    'BlendshapeFrameRawData',
)


@json_model()
class BlendshapeFrameRawData():
    _position_deltas : Optional[bytes] = field(default=None, init=False) # float3
    _normal_deltas : Optional[bytes] = field(default=None, init=False) # float3
    _tangent_deltas : Optional[bytes] = field(default=None, init=False) # float3

    # Position of the frame within the blendshape animation
    # When blendshape has only a single frame, this should be set to 1.0
    # With multiple frames per blendshape, this determines the position at which this set of deltas is fully applied.
    position : float = json_element("position", float, default=MISSING)

    # Initializes the position deltas.
    init_position_deltas : InitVar[Optional[List['Float3']]] = None

    # Initializes the normal deltas.
    init_normal_deltas : InitVar[Optional[List['Float3']]] = None

    # Initializes the tangent deltas.
    init_tangent_deltas : InitVar[Optional[List['Float3']]] = None

    def __post_init__(
        self,
        init_position_deltas : Optional[List['Float3']],
        init_normal_deltas : Optional[List['Float3']],
        init_tangent_deltas : Optional[List['Float3']]
    ):
        if init_position_deltas:
            self.position_deltas = init_position_deltas
        if init_normal_deltas:
            self.normal_deltas = init_normal_deltas
        if init_tangent_deltas:
            self.tangent_deltas = init_tangent_deltas

    @property
    def position_deltas(self) -> List['Float3']:
        if not self._position_deltas:
            raise ValueError("Position deltas were never provided!")
        
        arr = array("f")
        arr.frombytes(self._position_deltas)
        return list(pack_vectors_float3(iter(arr)))

    @position_deltas.setter
    def position_deltas(self, position_deltas : List['Float3']):
        self._position_deltas = array("f", unpack_vectors_float3(iter(position_deltas))).tobytes()
    
    @property
    def normal_deltas(self) -> List['Float3']:
        if not self._normal_deltas:
            raise ValueError("Position deltas were never provided!")
        
        arr = array("f")
        arr.frombytes(self._normal_deltas)
        return list(pack_vectors_float3(iter(arr)))

    @normal_deltas.setter
    def normal_deltas(self, normal_deltas : List['Float3']):
        self._normal_deltas = array("f", unpack_vectors_float3(iter(normal_deltas))).tobytes()

    @property
    def tangent_deltas(self) -> List['Float3']:
        if not self._tangent_deltas:
            raise ValueError("Position deltas were never provided!")
        
        arr = array("f")
        arr.frombytes(self._tangent_deltas)
        return list(pack_vectors_float3(iter(arr)))

    @tangent_deltas.setter
    def tangent_deltas(self, tangent_deltas : List['Float3']):
        self._tangent_deltas = array("f", unpack_vectors_float3(iter(tangent_deltas))).tobytes()

    def _get_binary_data(self, import_msg : 'ImportMeshRawData', blendshape_raw_data : 'BlendshapeRawData') -> bytes:
        expected_data_size = import_msg.vertex_count * 4 * 3 # 3x float (4 bytes) per vertex
        data = bytearray()

        if not self._position_deltas:
            raise ValueError("Position deltas were never provided!")    
        elif len(self._position_deltas) != expected_data_size:
            raise ValueError(f"Position deltas size mismatch! Expected: {expected_data_size} (For mesh with {import_msg.vertex_count} vertices), Actual: {len(self._position_deltas)}")
        else:
            data.extend(self._position_deltas)

        if blendshape_raw_data.has_normal_deltas:
            if not self._normal_deltas:
                raise ValueError("Normal deltas were never provided!")
            elif len(self._normal_deltas) != expected_data_size:
                raise ValueError(f"Normal deltas size mismatch! Expected: {expected_data_size} (For mesh with {import_msg.vertex_count} vertices), Actual: {len(self._position_deltas)}")
            else:
                data.extend(self._normal_deltas)
        
        if blendshape_raw_data.has_tangent_deltas:
            if not self._tangent_deltas:
                raise ValueError("Tangent deltas were never provided!")
            elif len(self._tangent_deltas) != expected_data_size:
                raise ValueError(f"Tangent deltas size mismatch! Expected: {expected_data_size} (For mesh with {import_msg.vertex_count} vertices), Actual: {len(self._position_deltas)}")
            else:
                data.extend(self._tangent_deltas)

        return data
