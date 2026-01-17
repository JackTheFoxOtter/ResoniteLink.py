from .blendshape_frame import BlendshapeFrame
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("blendshape") # TODO: Anonymous
@dataclass(slots=True)
class Blendshape():
    # Name of the Blendshape.
    name : Annotated[str, JSONProperty("name")]

    # Frames that compose this blendshape.
    # Blendshapes need at least 1 frame.
    frames : Annotated[List[BlendshapeFrame], JSONProperty("frames", model_type_name="blendshapeFrame")] = MISSING
