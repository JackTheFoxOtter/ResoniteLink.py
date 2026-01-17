from .submesh_raw_data import SubmeshRawData
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("triangleSubmeshRawData") # TODO: Anonymous model
@dataclass(slots=True)
class TriangleSubmeshRawData(SubmeshRawData):
    triangle_count : Annotated[int, JSONProperty("triangleCount")] = MISSING

    @property
    def indices_count(self) -> int:
        return self.triangle_count * 3
