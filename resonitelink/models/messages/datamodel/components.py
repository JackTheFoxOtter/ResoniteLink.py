from resonitelink.models.messages import MessageBase
from resonitelink.json.models import model, JSONProperty
from typing import Annotated, Any

@model("getComponent")
class GetComponent(MessageBase):
    component_id : Annotated[str, JSONProperty("componentId")]

@model("addComponent")
class AddComponent(MessageBase):
    data : Annotated[Any, JSONProperty("data")] # TODO: This should be of type component
    container_slot_id : Annotated[str, JSONProperty("containerSlotId")]

@model("updateComponent")
class UpdateComponent(MessageBase):
    data : Annotated[Any, JSONProperty("data")] # TODO: This should be of type component

@model("removeComponent")
class RemoveComponent(MessageBase):
    component_id : Annotated[str, JSONProperty("componentId")]
