from resonitelink.models.datamodel import Slot
from resonitelink.models.messages import BaseMessage
from resonitelink.json import MISSING, json_model, JSONProperty
from dataclasses import dataclass
from typing import Annotated


@dataclass
@json_model("getSlot")
class GetSlot(BaseMessage):
    slot_id : Annotated[str, JSONProperty("slotId")] = MISSING
    depth : Annotated[int, JSONProperty("depth")] = MISSING
    include_component_data : Annotated[bool, JSONProperty("includeComponentData")] = MISSING


@dataclass
@json_model("addSlot")
class AddSlot(BaseMessage):
    data : Annotated[Slot, JSONProperty("data")] = MISSING


@dataclass
@json_model("updateSlot")
class UpdateSlot(BaseMessage):
    data : Annotated[Slot, JSONProperty("data")] = MISSING


@dataclass
@json_model("removeSlot")
class RemoveSlot(BaseMessage):
    slot_id : Annotated[str, JSONProperty("slotId")] = MISSING
