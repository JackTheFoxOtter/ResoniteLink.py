#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("t_floatQ")
@dataclass(slots=True)
class FloatQ():
    x : Annotated[float, JSONProperty("x")] = MISSING
    y : Annotated[float, JSONProperty("y")] = MISSING
    z : Annotated[float, JSONProperty("z")] = MISSING
    w : Annotated[float, JSONProperty("w")] = MISSING


@json_model("t_doubleQ")
@dataclass(slots=True)
class DoubleQ():
    x : Annotated[float, JSONProperty("x")] = MISSING
    y : Annotated[float, JSONProperty("y")] = MISSING
    z : Annotated[float, JSONProperty("z")] = MISSING
    w : Annotated[float, JSONProperty("w")] = MISSING
