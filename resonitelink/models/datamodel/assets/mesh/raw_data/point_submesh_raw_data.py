from .submesh_raw_data import SubmeshRawData
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("pointSubmeshRawData") # TODO: Anonymous model
@dataclass(slots=True)
class PointSubmeshRawData(SubmeshRawData):
    point_count : Annotated[int, JSONProperty("pointCount")] = MISSING

    @property
    def indices_count(self) -> int:
        return self.point_count
