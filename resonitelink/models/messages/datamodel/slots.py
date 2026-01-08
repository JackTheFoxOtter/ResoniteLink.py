from resonitelink.models.messages import MessageBase
from resonitelink.json.models import model, JSONProperty
from typing import Annotated, Any

@model("getSlot")
class GetSlot(MessageBase):
    slot_id : Annotated[str, JSONProperty("slotId")]
    depth : Annotated[int, JSONProperty("depth")]
    include_component_data : Annotated[bool, JSONProperty("includeComponentData")]

@model("addSlot")
class AddSlot(MessageBase):
    data : Annotated[Any, JSONProperty("data")] # TODO: This should be of type Slot

@model("updateSlot")
class UpdateSlot(MessageBase):
    data : Annotated[Any, JSONProperty("data")] # TODO: This should be of type Slot

@model("removeSlot")
class RemoveSlot(MessageBase):
    slot_id : Annotated[str, JSONProperty("slotId")]
