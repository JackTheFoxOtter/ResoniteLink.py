#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#      >==============================================================================<
from resonitelink.json import JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("floatQ")
@dataclass(slots=True)
class FloatQ():
    x : Annotated[float, JSONProperty("x")]
    y : Annotated[float, JSONProperty("y")]
    z : Annotated[float, JSONProperty("z")]
    w : Annotated[float, JSONProperty("w")]


@json_model("doubleQ")
@dataclass(slots=True)
class DoubleQ():
    x : Annotated[float, JSONProperty("x")]
    y : Annotated[float, JSONProperty("y")]
    z : Annotated[float, JSONProperty("z")]
    w : Annotated[float, JSONProperty("w")]
