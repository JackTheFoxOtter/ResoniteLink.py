from resonitelink.models.messages import BaseMessage
from resonitelink.json import MISSING, json_model, JSONProperty
from dataclasses import dataclass
from typing import Annotated, Any


@dataclass
@json_model("getComponent")
class GetComponent(BaseMessage):
    component_id : Annotated[str, JSONProperty("componentId")] = MISSING


@dataclass
@json_model("addComponent")
class AddComponent(BaseMessage):
    data : Annotated[Any, JSONProperty("data")] = MISSING # TODO: This should be of type Component
    container_slot_id : Annotated[str, JSONProperty("containerSlotId")] = MISSING


@dataclass
@json_model("updateComponent")
class UpdateComponent(BaseMessage):
    data : Annotated[Any, JSONProperty("data")] = MISSING # TODO: This should be of type Component


@dataclass
@json_model("removeComponent")
class RemoveComponent(BaseMessage):
    component_id : Annotated[str, JSONProperty("componentId")] = MISSING
