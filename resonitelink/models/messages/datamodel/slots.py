from resonitelink.models.messages import MessageBase
from resonitelink.json.models import json_model, JSONProperty
from typing import Annotated, Any

@json_model("getSlot")
class GetSlot(MessageBase):
    slot_id : Annotated[str, JSONProperty("slotId")]
    depth : Annotated[int, JSONProperty("depth")]
    include_component_data : Annotated[bool, JSONProperty("includeComponentData")]

@json_model("addSlot")
class AddSlot(MessageBase):
    data : Annotated[Any, JSONProperty("data")] # TODO: This should be of type Slot

@json_model("updateSlot")
class UpdateSlot(MessageBase):
    data : Annotated[Any, JSONProperty("data")] # TODO: This should be of type Slot

@json_model("removeSlot")
class RemoveSlot(MessageBase):
    slot_id : Annotated[str, JSONProperty("slotId")]
    fake_get_slot : Annotated[GetSlot, JSONProperty("fakeGetSlotForRecursiveTesting")]
