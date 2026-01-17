from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("boneWeight") # TODO: Anonymous
@dataclass(slots=True)
class BoneWeight():
    """
    Maps vertex to a specific bone with specific weight.
    
    """
    # Index of the bone this maps too in the Bones list of the mesh.
    bone_index : Annotated[int, JSONProperty("boneIndex")] = MISSING

    # Weight from 0...1 that influences how much is this vertex affected by the bone.
    weight : Annotated[float, JSONProperty("weight")] = MISSING
