# from __future__ import annotations # Delayed evaluation of type hints (PEP 563)
from resonitelink.models.datamodel import Worker, Component, Reference, Field_Float3, Field_FloatQ, Field_Bool, Field_String, Field_Long
from resonitelink.json import MISSING, JSONProperty, JSONPropertyType, json_model
from dataclasses import dataclass, fields
from typing import Annotated, List


@json_model("slot")
@dataclass(slots=False)
class Slot(Worker):
    parent : Annotated[Reference, JSONProperty("parent", model_type_name="reference")] = MISSING
    position : Annotated[Field_Float3, JSONProperty("position", model_type_name="float3")] = MISSING
    rotation : Annotated[Field_FloatQ, JSONProperty("rotation", model_type_name="floatQ")] = MISSING
    scale : Annotated[Field_Float3, JSONProperty("scale", model_type_name="float3")] = MISSING
    is_active : Annotated[Field_Bool, JSONProperty("isActive", model_type_name="bool")] = MISSING
    is_persistent : Annotated[Field_Bool, JSONProperty("isPersistent", model_type_name="bool")] = MISSING
    name : Annotated[Field_String, JSONProperty("name", model_type_name="string")] = MISSING
    tag : Annotated[Field_String, JSONProperty("tag", model_type_name="string")] = MISSING
    order_offset : Annotated[Field_Long, JSONProperty("orderOffset", model_type_name="long")] = MISSING

    components : Annotated[List[Component], JSONProperty("components", model_type_name="component", property_type=JSONPropertyType.LIST)] = MISSING
    children : Annotated[List['Slot'], JSONProperty("children", model_type_name="slot", property_type=JSONPropertyType.LIST)] = MISSING

    # Special Slot references
    Root = Reference(target_id="Root", target_type="slot")
