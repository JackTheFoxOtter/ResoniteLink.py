from resonitelink.models.datamodel import Worker, Reference
from resonitelink.json import JSONProperty, json_model
from typing import Annotated, Any


@json_model("slot")
class Slot(Worker):
    parent : Annotated[Reference, JSONProperty("parent")]
    position : Annotated[Any, JSONProperty("position")] # TODO: Should be Field_Float3
    rotation : Annotated[Any, JSONProperty("rotation")] # TODO: Should be Field_FloatQ
    scale : Annotated[Any, JSONProperty("scale")] # TODO: Should be Field_Float3
    is_active : Annotated[Any, JSONProperty("isActive")] # TODO: Should be Field_Bool
    is_persistent : Annotated[Any, JSONProperty("isPersistent")] # TODO: Should be Field_Bool
    name : Annotated[Any, JSONProperty("name")] # TODO: Should be Field_String
    tag : Annotated[Any, JSONProperty("tag")] # TODO: Should be Field_String

    components : Annotated[Any, JSONProperty("components")] # TODO: Should be List[Component]
    children : Annotated[Any, JSONProperty("children")] # TODO: Should be List[Slot]
