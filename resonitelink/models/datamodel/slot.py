from resonitelink.models.datamodel import Worker, Reference
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, Any


@json_model("slot")
@dataclass(slots=False)
class Slot(Worker):
    parent : Annotated[Reference, JSONProperty("parent")] = MISSING
    position : Annotated[Any, JSONProperty("position")] = MISSING # TODO: Should be Field_Float3
    rotation : Annotated[Any, JSONProperty("rotation")] = MISSING # TODO: Should be Field_FloatQ
    scale : Annotated[Any, JSONProperty("scale")] = MISSING # TODO: Should be Field_Float3
    is_active : Annotated[Any, JSONProperty("isActive")] = MISSING # TODO: Should be Field_Bool
    is_persistent : Annotated[Any, JSONProperty("isPersistent")] = MISSING # TODO: Should be Field_Bool
    name : Annotated[Any, JSONProperty("name")] = MISSING # TODO: Should be Field_String
    tag : Annotated[Any, JSONProperty("tag")] = MISSING # TODO: Should be Field_String
    order_offset : Annotated[Any, JSONProperty("orderOffset")] = MISSING # TODO: Should be Field_Long

    components : Annotated[Any, JSONProperty("components")] = MISSING # TODO: Should be List[Component]
    children : Annotated[Any, JSONProperty("children")] = MISSING # TODO: Should be List[Slot]

    # Special Slot references
    Root = Reference(id=MISSING, target_id="Root", target_type="slot")
