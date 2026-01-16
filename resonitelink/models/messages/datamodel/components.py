from resonitelink.models.datamodel import Component
from resonitelink.models.messages import Message
from resonitelink.json import MISSING, json_model, JSONProperty
from dataclasses import dataclass
from typing import Annotated


@json_model("getComponent")
@dataclass(slots=True)
class GetComponent(Message):
    component_id : Annotated[str, JSONProperty("componentId")] = MISSING


@json_model("addComponent")
@dataclass(slots=True)
class AddComponent(Message):
    data : Annotated[Component, JSONProperty("data")] = MISSING
    container_slot_id : Annotated[str, JSONProperty("containerSlotId")] = MISSING


@json_model("updateComponent")
@dataclass(slots=True)
class UpdateComponent(Message):
    data : Annotated[Component, JSONProperty("data")] = MISSING


@json_model("removeComponent")
@dataclass(slots=True)
class RemoveComponent(Message):
    component_id : Annotated[str, JSONProperty("componentId")] = MISSING
