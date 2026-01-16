from resonitelink.models.datamodel import Field
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, Optional


@json_model("enum")
@dataclass(slots=True)
class Field_Enum(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    enum_type : Annotated[str, JSONProperty("enumType")] = MISSING

    @property
    def value_type_name(self) -> str:
        return "enum"


@json_model("enum?")
@dataclass(slots=True)
class Field_Nullable_Enum(Field):
    value : Annotated[Optional[str], JSONProperty("value")] = MISSING
    enum_type : Annotated[str, JSONProperty("enumType")] = MISSING

    @property
    def value_type_name(self) -> str:
        return "enum?"