from resonitelink.json import JSONProperty, json_model, MISSING
from dataclasses import dataclass
from typing import Annotated


@json_model("blendshapeFrameRawData") # TODO: This model should be anonymous
@dataclass(slots=True)
class BlendshapeFrameRawData():
    # Position of the frame within the blendshape animation
    # When blendshape has only a single frame, this should be set to 1.0
    # With multiple frames per blendshape, this determines the position at which this set of deltas is fully applied.
    position : Annotated[float, JSONProperty("position")] = MISSING
