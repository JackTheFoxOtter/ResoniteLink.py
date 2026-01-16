from resonitelink.models.responses import Response
from resonitelink.models.datamodel import Slot, Component
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("slotData")
@dataclass(slots=True)
class SlotData(Response):
    depth : Annotated[int, JSONProperty("depth")] = MISSING
    data : Annotated[Slot, JSONProperty("data", model_type_name="slot")] = MISSING


@json_model("componentData")
@dataclass(slots=True)
class ComponentData(Response):
    data : Annotated[Component, JSONProperty("data", model_type_name="component")] = MISSING


@json_model("assetData")
@dataclass(slots=True)
class AssetData(Response):
    asset_url : Annotated[str, JSONProperty("assetURL")] = MISSING
