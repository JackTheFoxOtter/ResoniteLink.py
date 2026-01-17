from .submesh import Submesh
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("pointSubmesh") # TODO: Anonymous model
@dataclass(slots=True)
class PointSubmesh(Submesh):
    vertex_indices : Annotated[List[int], JSONProperty("vertexIndices")] = MISSING
