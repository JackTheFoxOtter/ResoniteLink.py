#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#      >==============================================================================<
from resonitelink.json import JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("float2x2")
@dataclass(slots=True)
class Float2x2():
    m00 : Annotated[float, JSONProperty("m00")]
    m01 : Annotated[float, JSONProperty("m01")]
    m10 : Annotated[float, JSONProperty("m10")]
    m11 : Annotated[float, JSONProperty("m11")]


@json_model("float3x3")
@dataclass(slots=True)
class Float3x3():
    m00 : Annotated[float, JSONProperty("m00")]
    m01 : Annotated[float, JSONProperty("m01")]
    m02 : Annotated[float, JSONProperty("m02")]
    m10 : Annotated[float, JSONProperty("m10")]
    m11 : Annotated[float, JSONProperty("m11")]
    m12 : Annotated[float, JSONProperty("m12")]
    m20 : Annotated[float, JSONProperty("m20")]
    m21 : Annotated[float, JSONProperty("m21")]
    m22 : Annotated[float, JSONProperty("m22")]


@json_model("float4x4")
@dataclass(slots=True)
class Float4x4():
    m00 : Annotated[float, JSONProperty("m00")]
    m01 : Annotated[float, JSONProperty("m01")]
    m02 : Annotated[float, JSONProperty("m02")]
    m03 : Annotated[float, JSONProperty("m03")]
    m10 : Annotated[float, JSONProperty("m10")]
    m11 : Annotated[float, JSONProperty("m11")]
    m12 : Annotated[float, JSONProperty("m12")]
    m13 : Annotated[float, JSONProperty("m13")]
    m20 : Annotated[float, JSONProperty("m20")]
    m21 : Annotated[float, JSONProperty("m21")]
    m22 : Annotated[float, JSONProperty("m22")]
    m23 : Annotated[float, JSONProperty("m23")]
    m30 : Annotated[float, JSONProperty("m30")]
    m31 : Annotated[float, JSONProperty("m31")]
    m32 : Annotated[float, JSONProperty("m32")]
    m33 : Annotated[float, JSONProperty("m33")]


@json_model("double2x2")
@dataclass(slots=True)
class Double2x2():
    m00 : Annotated[float, JSONProperty("m00")]
    m01 : Annotated[float, JSONProperty("m01")]
    m10 : Annotated[float, JSONProperty("m10")]
    m11 : Annotated[float, JSONProperty("m11")]


@json_model("double3x3")
@dataclass(slots=True)
class Double3x3():
    m00 : Annotated[float, JSONProperty("m00")]
    m01 : Annotated[float, JSONProperty("m01")]
    m02 : Annotated[float, JSONProperty("m02")]
    m10 : Annotated[float, JSONProperty("m10")]
    m11 : Annotated[float, JSONProperty("m11")]
    m12 : Annotated[float, JSONProperty("m12")]
    m20 : Annotated[float, JSONProperty("m20")]
    m21 : Annotated[float, JSONProperty("m21")]
    m22 : Annotated[float, JSONProperty("m22")]


@json_model("double4x4")
@dataclass(slots=True)
class Double4x4():
    m00 : Annotated[float, JSONProperty("m00")]
    m01 : Annotated[float, JSONProperty("m01")]
    m02 : Annotated[float, JSONProperty("m02")]
    m03 : Annotated[float, JSONProperty("m03")]
    m10 : Annotated[float, JSONProperty("m10")]
    m11 : Annotated[float, JSONProperty("m11")]
    m12 : Annotated[float, JSONProperty("m12")]
    m13 : Annotated[float, JSONProperty("m13")]
    m20 : Annotated[float, JSONProperty("m20")]
    m21 : Annotated[float, JSONProperty("m21")]
    m22 : Annotated[float, JSONProperty("m22")]
    m23 : Annotated[float, JSONProperty("m23")]
    m30 : Annotated[float, JSONProperty("m30")]
    m31 : Annotated[float, JSONProperty("m31")]
    m32 : Annotated[float, JSONProperty("m32")]
    m33 : Annotated[float, JSONProperty("m33")]
