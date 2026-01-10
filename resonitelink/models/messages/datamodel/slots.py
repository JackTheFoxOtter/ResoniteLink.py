from resonitelink.models.datamodel import Slot
from resonitelink.models.messages import BaseMessage
from resonitelink.json.models import json_model, JSONProperty
from typing import Annotated

@json_model("getSlot")
class GetSlot(BaseMessage):
    slot_id : Annotated[str, JSONProperty("slotId")]
    depth : Annotated[int, JSONProperty("depth")]
    include_component_data : Annotated[bool, JSONProperty("includeComponentData")]

@json_model("addSlot")
class AddSlot(BaseMessage):
    data : Annotated[Slot, JSONProperty("data")]

@json_model("updateSlot")
class UpdateSlot(BaseMessage):
    data : Annotated[Slot, JSONProperty("data")]

@json_model("removeSlot")
class RemoveSlot(BaseMessage):
    slot_id : Annotated[str, JSONProperty("slotId")]
    fake_get_slot : Annotated[GetSlot, JSONProperty("fakeGetSlotForRecursiveTesting")]
