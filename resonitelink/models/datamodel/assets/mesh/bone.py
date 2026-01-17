from resonitelink.models.datamodel import Float4x4
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("bone") # TODO: This model should be anonymous
@dataclass(slots=True)
class Bone():
    # Name of the bone.
    # This generally doesn't have much actual function for mesh data, but is useful for references and debugging.
    name : Annotated[str, JSONProperty("name")] = MISSING

    # The bind pose of the bone - its default transform in model space.
    #This is essentially the pose of the bone relative to the vertices where the vertices bound to it will be in their original spot. 
    bind_pose : Annotated[Float4x4, JSONProperty("bindPose")] = MISSING
