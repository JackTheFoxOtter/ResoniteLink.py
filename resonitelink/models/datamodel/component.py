from resonitelink.models.datamodel import Worker, Member
from resonitelink.json import MISSING, JSONProperty, JSONPropertyType, json_model
from dataclasses import dataclass, field
from typing import Annotated, Dict


@json_model("component")
@dataclass(slots=False)
class Component(Worker):
    component_type : Annotated[str, JSONProperty("componentType")] = MISSING
    members : Annotated[Dict[str, Member], JSONProperty("members", property_type=JSONPropertyType.DICT)] = MISSING
