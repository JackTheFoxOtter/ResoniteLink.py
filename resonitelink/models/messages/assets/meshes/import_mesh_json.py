from resonitelink.models.datamodel.assets.mesh import Vertex, Submesh, Bone, Blendshape
from resonitelink.models.messages import Message
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("importMeshJSON")
@dataclass(slots=True)
class ImportMeshJSON(Message):
    """
    Imports a mesh asset from purely JSON definition.
    This is pretty verbose, so it's recommended only for smaller meshes, but is supported for
    convenience and ease of implementation & experimentation, at the cost of efficiency.
    If possible, it's recommended to use ImportMeshRawData for better efficiency.

    """
    #  Vertices of this mesh. These are shared across sub-meshes.
    vertices : Annotated[List[Vertex], JSONProperty("vertices", model_type_name="vertex")] = MISSING
    
    # List of submeshes (points, triangles...) representing this mesh.
    # Meshes will typically have at least one submesh.
    # Each submesh uses indicies of the vertices for its primitives.
    submeshes : Annotated[List[Submesh], JSONProperty("submeshes", model_type_name="submesh")] = MISSING

    # Bones of the mesh when data represents a skinned mesh.
    # These will be referred to by their index from vertex data.
    bones : Annotated[List[Bone], JSONProperty("bones", model_type_name="bone")] = MISSING

    # Blendshapes of this mesh.
    # These allow modifying the vertex positions, normals & tangents for animations such as facial expressions.
    blendshapes : Annotated[List[Blendshape], JSONProperty("blendshapes", model_type_name="blendshape")] = MISSING
