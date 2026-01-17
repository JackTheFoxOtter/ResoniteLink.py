from .blendshape_frame_raw_data import BlendshapeFrameRawData
from resonitelink.json import JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("blendshapeRawData") # TODO: This model should be anonymous
@dataclass(slots=True)
class BlendshapeRawData():
    # Name of the blendshape.
    name : Annotated[str, JSONProperty("name")]

    # Indicates if this blenshape has normal datas.
    has_normal_deltas : Annotated[bool, JSONProperty("hasNormalDeltas")]

    # Indicates if this blendshape has tangent deltas.
    has_tangent_deltas : Annotated[bool, JSONProperty("hasTangentDeltas")]

    # Frames that compose this blendshape.
    # Blendshapes need at least 1 frame.
    frames : Annotated[List[BlendshapeFrameRawData], JSONProperty("frames", model_type_name="blendshapeFrameRawData")]
