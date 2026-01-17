from resonitelink.models.datamodel import Float2, Float3, Float4
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated
from abc import ABC


@dataclass(slots=True)
class UV_Coordinate(ABC):
    pass


@json_model("2D") # TODO: Bound to UV_Coordinate!
@dataclass(slots=True)
class UV2D_Coordinate(UV_Coordinate):
    uv : Annotated[Float2, JSONProperty("uv", model_type_name="t_float2")] = MISSING


@json_model("3D") # TODO: Bound to UV_Coordinate!
@dataclass(slots=True)
class UV3D_Coordinate(UV_Coordinate):
    uv : Annotated[Float3, JSONProperty("uv", model_type_name="t_float3")] = MISSING


@json_model("4D") # TODO: Bound to UV_Coordinate!
@dataclass(slots=True)
class UV4D_Coordinate(UV_Coordinate):
    uv : Annotated[Float4, JSONProperty("uv", model_type_name="t_float4")] = MISSING
