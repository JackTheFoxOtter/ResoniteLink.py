from resonitelink.models.datamodel.assets.mesh import Bone, SubmeshRawData, BlendshapeRawData
from resonitelink.models.messages import BinaryPayloadMessage
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("importMeshRawData")
@dataclass(slots=True)
class ImportMeshRawData(BinaryPayloadMessage):
    # Number of vertices in this mesh.
    vertex_count : Annotated[int, JSONProperty("vertexCount")] = MISSING
    
    # Do vertices have normals?
    has_normals : Annotated[bool, JSONProperty("hasNormals")] = MISSING
    
    # Do vertices have tangents?
    has_tangents : Annotated[bool, JSONProperty("hasTangents")] = MISSING
    
    # Do vertices have colors?
    has_colors : Annotated[bool, JSONProperty("hasColors")] = MISSING
    
    # How many bone weights does each vertex have.
    # If some vertices have fewer bone weights, use weight of 0 for remainder bindings.
    bone_weight_count : Annotated[int, JSONProperty("boneWeightCount")] = MISSING
    
    # Configuration of UV channels for this mesh.
    # Each entry represents one UV channel of the mesh.
    # Number indicates number of UV dimensions. This must be between 2 and 4 (inclusive).
    uv_channel_dimensions : Annotated[List[int], JSONProperty("uvChannelDimensions")] = MISSING

    # Submeshes that form this mesh. Meshes will typically have at least one submesh.
    submeshes : Annotated[List[SubmeshRawData], JSONProperty("submeshes")] = MISSING

    # Blendshapes of this mesh.
    # These allow modifying the vertex positions, normals & tangents for animations such as facial expressions.
    blendshapes : Annotated[List[BlendshapeRawData], JSONProperty("blendshapes")] = MISSING

    # Bones of the mesh when data represents a skinned mesh.
    # These will be referred to by their index from vertex data.
    bones : Annotated[List[Bone], JSONProperty("bones")] = MISSING
