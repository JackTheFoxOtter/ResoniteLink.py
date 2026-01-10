from resonitelink.models.messages import BaseMessage
from resonitelink.json.models import json_model, JSONProperty
from typing import Annotated, Any

@json_model("getComponent")
class GetComponent(BaseMessage):
    component_id : Annotated[str, JSONProperty("componentId")]

@json_model("addComponent")
class AddComponent(BaseMessage):
    data : Annotated[Any, JSONProperty("data")] # TODO: This should be of type Component
    container_slot_id : Annotated[str, JSONProperty("containerSlotId")]

@json_model("updateComponent")
class UpdateComponent(BaseMessage):
    data : Annotated[Any, JSONProperty("data")] # TODO: This should be of type Component

@json_model("removeComponent")
class RemoveComponent(BaseMessage):
    component_id : Annotated[str, JSONProperty("componentId")]
