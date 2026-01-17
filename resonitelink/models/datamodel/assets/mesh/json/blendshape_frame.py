from resonitelink.models.datamodel import Float3
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("blendshapeFrame") # TODO: Anonymous
@dataclass(slots=True)
class BlendshapeFrame():
    # Position of the frame within the blendshape animation.
    # When blendshape has only a single frame, this should be set to 1.0.
    # With multiple frames per blendshape, this determines the position at which this set of deltas is fully applied.
    position : Annotated[float, JSONProperty("position")] = MISSING

    # Delta values for vertex positions of this blendshape frame.
    # Number of deltas MUST match number of vertices.
    position_deltas : Annotated[List[Float3], JSONProperty("positionDeltas", model_type_name="t_float3")] = MISSING

    # Optional. Delta values for vertex normals of this blendshape frame.
    # Number of deltas MUST match number of vertices.
    normal_deltas : Annotated[List[Float3], JSONProperty("normalDeltas", model_type_name="t_float3")] = MISSING

    # Optional. Delta values for vertex tangents of this blendshape frame.
    # Number of deltas MUST match number of vertices.
    tangent_deltas : Annotated[List[Float3], JSONProperty("tangentDeltas", model_type_name="t_float3")] = MISSING
