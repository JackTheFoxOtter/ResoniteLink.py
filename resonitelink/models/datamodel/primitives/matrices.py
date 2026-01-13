#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("t_float2x2")
@dataclass(slots=True)
class Float2x2():
    m00 : Annotated[float, JSONProperty("m00")] = MISSING
    m01 : Annotated[float, JSONProperty("m01")] = MISSING
    m10 : Annotated[float, JSONProperty("m10")] = MISSING
    m11 : Annotated[float, JSONProperty("m11")] = MISSING


@json_model("t_float3x3")
@dataclass(slots=True)
class Float3x3():
    m00 : Annotated[float, JSONProperty("m00")] = MISSING
    m01 : Annotated[float, JSONProperty("m01")] = MISSING
    m02 : Annotated[float, JSONProperty("m02")] = MISSING
    m10 : Annotated[float, JSONProperty("m10")] = MISSING
    m11 : Annotated[float, JSONProperty("m11")] = MISSING
    m12 : Annotated[float, JSONProperty("m12")] = MISSING
    m20 : Annotated[float, JSONProperty("m20")] = MISSING
    m21 : Annotated[float, JSONProperty("m21")] = MISSING
    m22 : Annotated[float, JSONProperty("m22")] = MISSING


@json_model("t_float4x4")
@dataclass(slots=True)
class Float4x4():
    m00 : Annotated[float, JSONProperty("m00")] = MISSING
    m01 : Annotated[float, JSONProperty("m01")] = MISSING
    m02 : Annotated[float, JSONProperty("m02")] = MISSING
    m03 : Annotated[float, JSONProperty("m03")] = MISSING
    m10 : Annotated[float, JSONProperty("m10")] = MISSING
    m11 : Annotated[float, JSONProperty("m11")] = MISSING
    m12 : Annotated[float, JSONProperty("m12")] = MISSING
    m13 : Annotated[float, JSONProperty("m13")] = MISSING
    m20 : Annotated[float, JSONProperty("m20")] = MISSING
    m21 : Annotated[float, JSONProperty("m21")] = MISSING
    m22 : Annotated[float, JSONProperty("m22")] = MISSING
    m23 : Annotated[float, JSONProperty("m23")] = MISSING
    m30 : Annotated[float, JSONProperty("m30")] = MISSING
    m31 : Annotated[float, JSONProperty("m31")] = MISSING
    m32 : Annotated[float, JSONProperty("m32")] = MISSING
    m33 : Annotated[float, JSONProperty("m33")] = MISSING


@json_model("t_double2x2")
@dataclass(slots=True)
class Double2x2():
    m00 : Annotated[float, JSONProperty("m00")] = MISSING
    m01 : Annotated[float, JSONProperty("m01")] = MISSING
    m10 : Annotated[float, JSONProperty("m10")] = MISSING
    m11 : Annotated[float, JSONProperty("m11")] = MISSING


@json_model("t_double3x3")
@dataclass(slots=True)
class Double3x3():
    m00 : Annotated[float, JSONProperty("m00")] = MISSING
    m01 : Annotated[float, JSONProperty("m01")] = MISSING
    m02 : Annotated[float, JSONProperty("m02")] = MISSING
    m10 : Annotated[float, JSONProperty("m10")] = MISSING
    m11 : Annotated[float, JSONProperty("m11")] = MISSING
    m12 : Annotated[float, JSONProperty("m12")] = MISSING
    m20 : Annotated[float, JSONProperty("m20")] = MISSING
    m21 : Annotated[float, JSONProperty("m21")] = MISSING
    m22 : Annotated[float, JSONProperty("m22")] = MISSING


@json_model("t_double4x4")
@dataclass(slots=True)
class Double4x4():
    m00 : Annotated[float, JSONProperty("m00")] = MISSING
    m01 : Annotated[float, JSONProperty("m01")] = MISSING
    m02 : Annotated[float, JSONProperty("m02")] = MISSING
    m03 : Annotated[float, JSONProperty("m03")] = MISSING
    m10 : Annotated[float, JSONProperty("m10")] = MISSING
    m11 : Annotated[float, JSONProperty("m11")] = MISSING
    m12 : Annotated[float, JSONProperty("m12")] = MISSING
    m13 : Annotated[float, JSONProperty("m13")] = MISSING
    m20 : Annotated[float, JSONProperty("m20")] = MISSING
    m21 : Annotated[float, JSONProperty("m21")] = MISSING
    m22 : Annotated[float, JSONProperty("m22")] = MISSING
    m23 : Annotated[float, JSONProperty("m23")] = MISSING
    m30 : Annotated[float, JSONProperty("m30")] = MISSING
    m31 : Annotated[float, JSONProperty("m31")] = MISSING
    m32 : Annotated[float, JSONProperty("m32")] = MISSING
    m33 : Annotated[float, JSONProperty("m33")] = MISSING
