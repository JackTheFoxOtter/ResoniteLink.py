from dataclasses import InitVar, field
from typing import Optional, List
from array import array
import struct

from resonitelink.models.datamodel.primitives import Float3, Float4, Color
from resonitelink.utils.vector_tools import pack_vectors_float3, unpack_vectors_float3, pack_vectors_float4, unpack_vectors_float4, pack_vectors_color, unpack_vectors_color
from resonitelink.models.assets.mesh import SubmeshRawData, BlendshapeRawData, Bone, BoneWeightRawData
from resonitelink.models.messages import Message, BinaryPayloadMessage
from resonitelink.json import MISSING, json_model, json_element, json_list


__all__ = (
    'ImportMeshRawData',
)


@json_model("importMeshRawData", Message)
class ImportMeshRawData(BinaryPayloadMessage):
    _positions : Optional[bytes] = field(default=None, init=False) # float3
    _normals : Optional[bytes] = field(default=None, init=False) # float3
    _tangents : Optional[bytes] = field(default=None, init=False) # float4
    _colors : Optional[bytes] = field(default=None, init=False) # color (float4: rgba)
    _bone_weights : Optional[bytes] = field(default=None, init=False) # struct{ int, float } (bone_index, weight)
    _uvs : Optional[List[bytes]] = field(default=None, init=False) # float

    # Number of vertices in this mesh.
    vertex_count : int = json_element("vertexCount", int, default=MISSING, init=False)

    # Initializes the positions of the mesh.
    init_positions : InitVar[Optional[List[Float3]]] = None
    
    # Do vertices have normals?
    has_normals : bool = json_element("hasNormals", bool, default=MISSING, init=False)

    # Initializes the vertex normals of the mesh.
    init_normals : InitVar[Optional[List[Float3]]] = None
    
    # Do vertices have tangents?
    has_tangents : bool = json_element("hasTangents", bool, default=MISSING, init=False)

    # Initializes the vertex tangents of the mesh.
    init_tangents : InitVar[Optional[List[Float4]]] = None
    
    # Do vertices have colors?
    has_colors : bool = json_element("hasColors", bool, default=MISSING, init=False)
    
    # Initializes the vertex colors of the mesh.
    init_colors : InitVar[Optional[List[Color]]] = None

    # Configuration of UV channels for this mesh.
    # Each entry represents one UV channel of the mesh.
    # Number indicates number of UV dimensions. This must be between 2 and 4 (inclusive).
    uv_channel_dimensions : List[int] = json_list("uvChannelDimensions", int, default=MISSING)

    # Initializes the UVs of the mesh.
    init_uvs : InitVar[Optional[List[List[float]]]] = None

    # How many bone weights does each vertex have.
    # If some vertices have fewer bone weights, use weight of 0 for remainder bindings.
    bone_weight_count : int = json_element("boneWeightCount", int, default=MISSING, init=False)

    # Initializes the bone weights.
    init_bone_weights : InitVar[Optional[List[BoneWeightRawData]]] = None

    # Submeshes that form this mesh. Meshes will typically have at least one submesh.
    submeshes : List[SubmeshRawData] = json_list("submeshes", SubmeshRawData, default=MISSING)

    # Blendshapes of this mesh.
    # These allow modifying the vertex positions, normals & tangents for animations such as facial expressions.
    blendshapes : List[BlendshapeRawData] = json_list("blendshapes", BlendshapeRawData, default=MISSING) # TODO: Pack into binary payload

    # Bones of the mesh when data represents a skinned mesh.
    # These will be referred to by their index from vertex data.
    bones : List[Bone] = json_list("bones", Bone, default=MISSING)

    def __post_init__(
        self, 
        init_positions : Optional[List[Float3]],
        init_normals : Optional[List[Float3]],
        init_tangents : Optional[List[Float4]],
        init_colors : Optional[List[Color]],
        init_uvs : Optional[List[List[float]]],
        init_bone_weights : Optional[List[BoneWeightRawData]],
    ):
        if init_positions:
            self.vertex_count = len(init_positions)
            self.positions = init_positions
        if init_normals:
            self.has_normals = True
            self.normals = init_normals
        if init_tangents:
            self.has_tangents = True
            self.tangents = init_tangents
        if init_colors:
            self.has_colors = True
            self.colors = init_colors
        if init_uvs:
            self.uvs = init_uvs
        if init_bone_weights:
            self.bone_weight_count = len(init_bone_weights)
            self.bone_weights = init_bone_weights
    
    @property
    def positions(self) -> List[Float3]:
        if not self._positions:
            raise ValueError("Positions were never provided!")
        
        arr = array("f")
        arr.frombytes(self._positions)
        return list(pack_vectors_float3(iter(arr)))
    
    @positions.setter
    def positions(self, vectors : List[Float3]):
        if len(vectors) != self.vertex_count:
            raise ValueError(f"Expected {self.vertex_count} vertex positions, but got {len(vectors)} indices.")
        
        self._positions = array("f", unpack_vectors_float3(iter(vectors))).tobytes()
    
    @property
    def normals(self) -> List[Float3]:
        if not self._normals:
            raise ValueError("Normals were never provided!")
        
        arr = array("f")
        arr.frombytes(self._normals)
        return list(pack_vectors_float3(iter(arr)))
    
    @normals.setter
    def normals(self, normals : List[Float3]):
        if len(normals) != self.vertex_count:
            raise ValueError(f"Expected {self.vertex_count} normals, but got {len(normals)} normals.")
        
        self._normals = array("f", unpack_vectors_float3(iter(normals))).tobytes()
    
    @property
    def tangents(self) -> List[Float4]:
        if not self._tangents:
            raise ValueError("Tangents were never provided!")
        
        arr = array("f")
        arr.frombytes(self._tangents)
        return list(pack_vectors_float4(iter(arr)))
    
    @tangents.setter
    def tangents(self, tangents : List[Float4]):
        if len(tangents) != self.vertex_count:
            raise ValueError(f"Expected {self.vertex_count} tangents, but got {len(tangents)} tangents.")
        
        self._tangents = array("f", unpack_vectors_float4(iter(tangents))).tobytes()

    @property
    def colors(self) -> List[Color]:
        if not self._colors:
            raise ValueError("Colors were never provided!")
        
        arr = array("f")
        arr.frombytes(self._colors)
        return list(pack_vectors_color(iter(arr)))
    
    @colors.setter
    def colors(self, colors : List[Color]):
        if len(colors) != self.vertex_count:
            raise ValueError(f"Expected {self.vertex_count} vertex colors, but got {len(colors)} colors.")
        
        self._colors = array("f", unpack_vectors_color(iter(colors))).tobytes()
    
    @property
    def uvs(self) -> List[List[float]]:
        if not self._uvs:
            raise ValueError("UVs were never provided!")
        
        uvs : List[List[float]] = []
        for uv_data in self._uvs:
            arr = array("f")
            arr.frombytes(uv_data)
            uvs.append(list((iter(arr))))
        
        return uvs
    
    @uvs.setter
    def uvs(self, uvs : List[List[float]]):
        if not self.uv_channel_dimensions:
            raise ValueError("UV channel dimensions were never provided!")
        if len(uvs) != len(self.uv_channel_dimensions):
            raise ValueError(f"UV channel count missmatch: UV channel dimensions: {len(self.uv_channel_dimensions)}, UV channels: {len(uvs)}.")
        
        uv_data : List[bytes] = []
        for index, uv in enumerate(uvs):
            len_expected = self.uv_channel_dimensions[index] * self.vertex_count
            if len(uv) != len_expected:
                raise ValueError(f"UV size mismatch: Expected {len_expected} values for uv channel: {index}, dimensions: {self.uv_channel_dimensions[index]} & vertex count: {self.vertex_count}.")

            uv_data.append(array("f", uv).tobytes())
        
        self._uvs = uv_data
    
    @property
    def bone_weights(self) -> List[BoneWeightRawData]:
        if not self._bone_weights:
            raise ValueError("Bone weights were never provided!")
        
        return list([ BoneWeightRawData(tpl[0], tpl[1]) for tpl in struct.iter_unpack("if", self._bone_weights) ])
    
    @bone_weights.setter
    def bone_weights(self, bone_weights : List[BoneWeightRawData]):
        if len(bone_weights) != self.vertex_count:
            raise ValueError(f"Expected {self.vertex_count} vertex colors, but got {len(bone_weights)} colors.")
        
        arr = bytearray()
        for bone_weight in bone_weights:
            arr.extend(struct.pack("if", bone_weight.bone_index, bone_weight.weight))

        self._bone_weights = arr

    @property
    def raw_binary_payload(self) -> bytes:
        data = bytearray()

        if self._positions:
            data.extend(self._positions)
        
        if self._normals:
            data.extend(self._normals)
        
        if self._tangents:
            data.extend(self._tangents)
        
        if self._colors:
            data.extend(self._colors)
        
        if self._uvs:
            for uv_data in self._uvs:
                data.extend(uv_data)
        
        if self._bone_weights:
            data.extend(self._bone_weights)
        
        if self.submeshes:
            for submesh in self.submeshes:
                submesh.extend_binary_data(data, self)
        
        if self.blendshapes:
            for blendshape in self.blendshapes:
                blendshape.extend_binary_data(data, self)
        
        return data

    @raw_binary_payload.setter
    def raw_binary_payload(self, data : bytes):
        raise NotImplementedError()
