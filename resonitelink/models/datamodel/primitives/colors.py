from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("t_color")
@dataclass(slots=True)
class Color():
    r : Annotated[float, JSONProperty("r")] = MISSING
    g : Annotated[float, JSONProperty("g")] = MISSING
    b : Annotated[float, JSONProperty("b")] = MISSING
    a : Annotated[float, JSONProperty("a")] = MISSING


@json_model("t_colorX")
@dataclass(slots=True)
class ColorX():
    r : Annotated[float, JSONProperty("r")] = MISSING
    g : Annotated[float, JSONProperty("g")] = MISSING
    b : Annotated[float, JSONProperty("b")] = MISSING
    a : Annotated[float, JSONProperty("a")] = MISSING
    profile : Annotated[str, JSONProperty("profile")] = MISSING


@json_model("t_color32")
@dataclass(slots=True)
class Color32():
    r : Annotated[int, JSONProperty("r")] = MISSING
    g : Annotated[int, JSONProperty("g")] = MISSING
    b : Annotated[int, JSONProperty("b")] = MISSING
    a : Annotated[int, JSONProperty("a")] = MISSING
