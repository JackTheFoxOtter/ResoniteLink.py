#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#      >==============================================================================<
from resonitelink.models.datamodel.primitives import *
from resonitelink.models.datamodel.primitives_containers import *
from resonitelink.models.datamodel.sync_array import SyncArray
from decimal import Decimal
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List


@json_model("array_bool")
@dataclass(slots=True)
class Array_Bool(SyncArray):
    values : Annotated[List[bool], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool"


@json_model("array_byte")
@dataclass(slots=True)
class Array_Byte(SyncArray):
    values : Annotated[List[int], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte"


@json_model("array_sbyte")
@dataclass(slots=True)
class Array_SByte(SyncArray):
    values : Annotated[List[int], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte"


@json_model("array_ushort")
@dataclass(slots=True)
class Array_UShort(SyncArray):
    values : Annotated[List[int], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort"


@json_model("array_short")
@dataclass(slots=True)
class Array_Short(SyncArray):
    values : Annotated[List[int], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short"


@json_model("array_uint")
@dataclass(slots=True)
class Array_UInt(SyncArray):
    values : Annotated[List[int], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint"


@json_model("array_int")
@dataclass(slots=True)
class Array_Int(SyncArray):
    values : Annotated[List[int], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int"


@json_model("array_ulong")
@dataclass(slots=True)
class Array_ULong(SyncArray):
    values : Annotated[List[int], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong"


@json_model("array_long")
@dataclass(slots=True)
class Array_Long(SyncArray):
    values : Annotated[List[int], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long"


@json_model("array_float")
@dataclass(slots=True)
class Array_Float(SyncArray):
    values : Annotated[List[float], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float"


@json_model("array_double")
@dataclass(slots=True)
class Array_Double(SyncArray):
    values : Annotated[List[float], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double"


@json_model("array_decimal")
@dataclass(slots=True)
class Array_Decimal(SyncArray):
    values : Annotated[List[Decimal], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "decimal"


@json_model("array_char")
@dataclass(slots=True)
class Array_Char(SyncArray):
    values : Annotated[List[str], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "char"


@json_model("array_string")
@dataclass(slots=True)
class Array_String(SyncArray):
    values : Annotated[List[str], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "string"


@json_model("array_Uri")
@dataclass(slots=True)
class Array_Uri(SyncArray):
    values : Annotated[List[str], JSONProperty("values")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "Uri"


@json_model("array_color")
@dataclass(slots=True)
class Array_Color(SyncArray):
    values : Annotated[List[Color], JSONProperty("values", model_type_name="color")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color"


@json_model("array_colorX")
@dataclass(slots=True)
class Array_ColorX(SyncArray):
    values : Annotated[List[ColorX], JSONProperty("values", model_type_name="colorX")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "colorX"


@json_model("array_color32")
@dataclass(slots=True)
class Array_Color32(SyncArray):
    values : Annotated[List[Color32], JSONProperty("values", model_type_name="color32")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color32"


@json_model("array_floatQ")
@dataclass(slots=True)
class Array_FloatQ(SyncArray):
    values : Annotated[List[FloatQ], JSONProperty("values", model_type_name="floatQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "floatQ"


@json_model("array_doubleQ")
@dataclass(slots=True)
class Array_DoubleQ(SyncArray):
    values : Annotated[List[DoubleQ], JSONProperty("values", model_type_name="doubleQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ"


@json_model("array_bool2")
@dataclass(slots=True)
class Array_Bool2(SyncArray):
    values : Annotated[List[Bool2], JSONProperty("values", model_type_name="bool2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool2"


@json_model("array_bool3")
@dataclass(slots=True)
class Array_Bool3(SyncArray):
    values : Annotated[List[Bool3], JSONProperty("values", model_type_name="bool3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool3"


@json_model("array_bool4")
@dataclass(slots=True)
class Array_Bool4(SyncArray):
    values : Annotated[List[Bool4], JSONProperty("values", model_type_name="bool4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool4"


@json_model("array_byte2")
@dataclass(slots=True)
class Array_Byte2(SyncArray):
    values : Annotated[List[Byte2], JSONProperty("values", model_type_name="byte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte2"


@json_model("array_byte3")
@dataclass(slots=True)
class Array_Byte3(SyncArray):
    values : Annotated[List[Byte3], JSONProperty("values", model_type_name="byte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte3"


@json_model("array_byte4")
@dataclass(slots=True)
class Array_Byte4(SyncArray):
    values : Annotated[List[Byte4], JSONProperty("values", model_type_name="byte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte4"


@json_model("array_sbyte2")
@dataclass(slots=True)
class Array_Sbyte2(SyncArray):
    values : Annotated[List[SByte2], JSONProperty("values", model_type_name="sbyte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2"


@json_model("array_sbyte3")
@dataclass(slots=True)
class Array_Sbyte3(SyncArray):
    values : Annotated[List[SByte3], JSONProperty("values", model_type_name="sbyte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3"


@json_model("array_sbyte4")
@dataclass(slots=True)
class Array_Sbyte4(SyncArray):
    values : Annotated[List[SByte4], JSONProperty("values", model_type_name="sbyte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4"


@json_model("array_ushort2")
@dataclass(slots=True)
class Array_Ushort2(SyncArray):
    values : Annotated[List[UShort2], JSONProperty("values", model_type_name="ushort2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort2"


@json_model("array_ushort3")
@dataclass(slots=True)
class Array_Ushort3(SyncArray):
    values : Annotated[List[UShort3], JSONProperty("values", model_type_name="ushort3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort3"


@json_model("array_ushort4")
@dataclass(slots=True)
class Array_Ushort4(SyncArray):
    values : Annotated[List[UShort4], JSONProperty("values", model_type_name="ushort4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort4"


@json_model("array_short2")
@dataclass(slots=True)
class Array_Short2(SyncArray):
    values : Annotated[List[Short2], JSONProperty("values", model_type_name="short2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short2"


@json_model("array_short3")
@dataclass(slots=True)
class Array_Short3(SyncArray):
    values : Annotated[List[Short3], JSONProperty("values", model_type_name="short3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short3"


@json_model("array_short4")
@dataclass(slots=True)
class Array_Short4(SyncArray):
    values : Annotated[List[Short4], JSONProperty("values", model_type_name="short4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short4"


@json_model("array_uint2")
@dataclass(slots=True)
class Array_Uint2(SyncArray):
    values : Annotated[List[UInt2], JSONProperty("values", model_type_name="uint2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint2"


@json_model("array_uint3")
@dataclass(slots=True)
class Array_Uint3(SyncArray):
    values : Annotated[List[UInt3], JSONProperty("values", model_type_name="uint3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint3"


@json_model("array_uint4")
@dataclass(slots=True)
class Array_Uint4(SyncArray):
    values : Annotated[List[UInt4], JSONProperty("values", model_type_name="uint4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint4"


@json_model("array_int2")
@dataclass(slots=True)
class Array_Int2(SyncArray):
    values : Annotated[List[Int2], JSONProperty("values", model_type_name="int2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int2"


@json_model("array_int3")
@dataclass(slots=True)
class Array_Int3(SyncArray):
    values : Annotated[List[Int3], JSONProperty("values", model_type_name="int3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int3"


@json_model("array_int4")
@dataclass(slots=True)
class Array_Int4(SyncArray):
    values : Annotated[List[Int4], JSONProperty("values", model_type_name="int4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int4"


@json_model("array_ulong2")
@dataclass(slots=True)
class Array_Ulong2(SyncArray):
    values : Annotated[List[ULong2], JSONProperty("values", model_type_name="ulong2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong2"


@json_model("array_ulong3")
@dataclass(slots=True)
class Array_Ulong3(SyncArray):
    values : Annotated[List[ULong3], JSONProperty("values", model_type_name="ulong3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong3"


@json_model("array_ulong4")
@dataclass(slots=True)
class Array_Ulong4(SyncArray):
    values : Annotated[List[ULong4], JSONProperty("values", model_type_name="ulong4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong4"


@json_model("array_long2")
@dataclass(slots=True)
class Array_Long2(SyncArray):
    values : Annotated[List[Long2], JSONProperty("values", model_type_name="long2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long2"


@json_model("array_long3")
@dataclass(slots=True)
class Array_Long3(SyncArray):
    values : Annotated[List[Long3], JSONProperty("values", model_type_name="long3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long3"


@json_model("array_long4")
@dataclass(slots=True)
class Array_Long4(SyncArray):
    values : Annotated[List[Long4], JSONProperty("values", model_type_name="long4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long4"


@json_model("array_float2")
@dataclass(slots=True)
class Array_Float2(SyncArray):
    values : Annotated[List[Float2], JSONProperty("values", model_type_name="float2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2"


@json_model("array_float3")
@dataclass(slots=True)
class Array_Float3(SyncArray):
    values : Annotated[List[Float3], JSONProperty("values", model_type_name="float3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3"


@json_model("array_float4")
@dataclass(slots=True)
class Array_Float4(SyncArray):
    values : Annotated[List[Float4], JSONProperty("values", model_type_name="float4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4"


@json_model("array_double2")
@dataclass(slots=True)
class Array_Double2(SyncArray):
    values : Annotated[List[Double2], JSONProperty("values", model_type_name="double2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2"


@json_model("array_double3")
@dataclass(slots=True)
class Array_Double3(SyncArray):
    values : Annotated[List[Double3], JSONProperty("values", model_type_name="double3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3"


@json_model("array_double4")
@dataclass(slots=True)
class Array_Double4(SyncArray):
    values : Annotated[List[Double4], JSONProperty("values", model_type_name="double4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4"


@json_model("array_float2x2")
@dataclass(slots=True)
class Array_Float2x2(SyncArray):
    values : Annotated[List[Float2x2], JSONProperty("values", model_type_name="float2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2x2"


@json_model("array_float3x3")
@dataclass(slots=True)
class Array_Float3x3(SyncArray):
    values : Annotated[List[Float3x3], JSONProperty("values", model_type_name="float3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3x3"


@json_model("array_float4x4")
@dataclass(slots=True)
class Array_Float4x4(SyncArray):
    values : Annotated[List[Float4x4], JSONProperty("values", model_type_name="float4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4x4"


@json_model("array_double2x2")
@dataclass(slots=True)
class Array_Double2x2(SyncArray):
    values : Annotated[List[Double2x2], JSONProperty("values", model_type_name="double2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2x2"


@json_model("array_double3x3")
@dataclass(slots=True)
class Array_Double3x3(SyncArray):
    values : Annotated[List[Double3x3], JSONProperty("values", model_type_name="double3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3x3"


@json_model("array_double4x4")
@dataclass(slots=True)
class Array_Double4x4(SyncArray):
    values : Annotated[List[Double4x4], JSONProperty("values", model_type_name="double4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4x4"
