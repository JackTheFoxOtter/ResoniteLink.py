from .uv_coordinate import UV_Coordinate
from .bone_weight import BoneWeight
from resonitelink.models.datamodel import Float2, Float3, Float4, Color
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("vertex")
@dataclass(slots=True)
class Vertex():
    """
    Defines a single vertex of a mesh. Position is mandatory field, but all other properties are optional.
    
    """
    # Position of the vertex.
    position : Annotated[Float3, JSONProperty("position", model_type_name="t_float3")]
    
    # Normal vector of the vertex.
    normal : Annotated[Float3, JSONProperty("normal", model_type_name="t_float3")]

    # Tangent vector of the vertex. The 4th component indicates direction of the binormal.
    # When specifying tangent, it's strongly recommended that normals are specified too.
    tangent : Annotated[Float3, JSONProperty("tangent", model_type_name="t_float3")]
    
    # Color of the vertex.
    color : Annotated[Color, JSONProperty("color", model_type_name="t_color")]
    
    # UV channel coordinates.
    # Each UV channel can have 2-4 dimensions.
    # Each vertex can have multiple UV channels.
    # The number of channels and dimensions for each MUST be same across all vertices.
    uvs : Annotated[List[UV_Coordinate], JSONProperty("uvs")]

    # Weights that define how much this vertex is affected by specific bones for skinned meshes.
    # The weights should add up to 1 across all the weights.
    bone_weights : Annotated[List[BoneWeight], JSONProperty("boneWeights", model_type_name="boneWeight")] = MISSING
