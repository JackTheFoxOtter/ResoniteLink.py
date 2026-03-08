#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from decimal import Decimal
from typing import List

from resonitelink.models.datamodel.primitives import *
from resonitelink.models.datamodel import Member, SyncArray
from resonitelink.types.aliases import *
from resonitelink.json import MISSING, json_model, json_list


__all__ = (
    'Array_Bool',
    'Array_Byte',
    'Array_SByte',
    'Array_UShort',
    'Array_Short',
    'Array_UInt',
    'Array_Int',
    'Array_ULong',
    'Array_Long',
    'Array_Float',
    'Array_Double',
    'Array_Decimal',
    'Array_Char',
    'Array_String',
    'Array_Uri',
    'Array_DateTime',
    'Array_TimeSpan',
    'Array_Color',
    'Array_ColorX',
    'Array_Color32',
    'Array_FloatQ',
    'Array_DoubleQ',
    'Array_Bool2',
    'Array_Bool3',
    'Array_Bool4',
    'Array_Byte2',
    'Array_Byte3',
    'Array_Byte4',
    'Array_Sbyte2',
    'Array_Sbyte3',
    'Array_Sbyte4',
    'Array_Ushort2',
    'Array_Ushort3',
    'Array_Ushort4',
    'Array_Short2',
    'Array_Short3',
    'Array_Short4',
    'Array_Uint2',
    'Array_Uint3',
    'Array_Uint4',
    'Array_Int2',
    'Array_Int3',
    'Array_Int4',
    'Array_Ulong2',
    'Array_Ulong3',
    'Array_Ulong4',
    'Array_Long2',
    'Array_Long3',
    'Array_Long4',
    'Array_Float2',
    'Array_Float3',
    'Array_Float4',
    'Array_Double2',
    'Array_Double3',
    'Array_Double4',
    'Array_Float2x2',
    'Array_Float3x3',
    'Array_Float4x4',
    'Array_Double2x2',
    'Array_Double3x3',
    'Array_Double4x4',
)


@json_model("bool[]", Member)
class Array_Bool(SyncArray):
    values : List[t_bool] = json_list("values", t_bool, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "bool"


@json_model("byte[]", Member)
class Array_Byte(SyncArray):
    values : List[t_byte] = json_list("values", t_byte, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "byte"


@json_model("sbyte[]", Member)
class Array_SByte(SyncArray):
    values : List[t_sbyte] = json_list("values", t_sbyte, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "sbyte"


@json_model("ushort[]", Member)
class Array_UShort(SyncArray):
    values : List[t_ushort] = json_list("values", t_ushort, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "ushort"


@json_model("short[]", Member)
class Array_Short(SyncArray):
    values : List[t_short] = json_list("values", t_short, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "short"


@json_model("uint[]", Member)
class Array_UInt(SyncArray):
    values : List[t_uint] = json_list("values", t_uint, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "uint"


@json_model("int[]", Member)
class Array_Int(SyncArray):
    values : List[t_int] = json_list("values", t_int, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "int"


@json_model("ulong[]", Member)
class Array_ULong(SyncArray):
    values : List[t_ulong] = json_list("values", t_ulong, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "ulong"


@json_model("long[]", Member)
class Array_Long(SyncArray):
    values : List[t_long] = json_list("values", t_long, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "long"


@json_model("float[]", Member)
class Array_Float(SyncArray):
    values : List[t_float] = json_list("values", t_float, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "float"


@json_model("double[]", Member)
class Array_Double(SyncArray):
    values : List[t_double] = json_list("values", t_double, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "double"


@json_model("decimal[]", Member)
class Array_Decimal(SyncArray):
    values : List[t_decimal] = json_list("values", t_decimal, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "decimal"


@json_model("char[]", Member)
class Array_Char(SyncArray):
    values : List[str] = json_list("values", str, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "char"


@json_model("string[]", Member)
class Array_String(SyncArray):
    values : List[str] = json_list("values", str, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "string"


@json_model("Uri[]", Member)
class Array_Uri(SyncArray):
    values : List[str] = json_list("values", str, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "Uri"


@json_model("DateTime[]", Member)
class Array_DateTime(SyncArray):
    values : List[str] = json_list("values", str, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "DateTime"


@json_model("TimeSpan[]", Member)
class Array_TimeSpan(SyncArray):
    values : List[str] = json_list("values", str, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "TimeSpan"


@json_model("color[]", Member)
class Array_Color(SyncArray):
    values : List[Color] = json_list("values", Color, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "color"


@json_model("colorX[]", Member)
class Array_ColorX(SyncArray):
    values : List[ColorX] = json_list("values", ColorX, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "colorX"


@json_model("color32[]", Member)
class Array_Color32(SyncArray):
    values : List[Color32] = json_list("values", Color32, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "color32"


@json_model("floatQ[]", Member)
class Array_FloatQ(SyncArray):
    values : List[FloatQ] = json_list("values", FloatQ, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "floatQ"


@json_model("doubleQ[]", Member)
class Array_DoubleQ(SyncArray):
    values : List[DoubleQ] = json_list("values", DoubleQ, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "doubleQ"


@json_model("bool2[]", Member)
class Array_Bool2(SyncArray):
    values : List[Bool2] = json_list("values", Bool2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "bool2"


@json_model("bool3[]", Member)
class Array_Bool3(SyncArray):
    values : List[Bool3] = json_list("values", Bool3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "bool3"


@json_model("bool4[]", Member)
class Array_Bool4(SyncArray):
    values : List[Bool4] = json_list("values", Bool4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "bool4"


@json_model("byte2[]", Member)
class Array_Byte2(SyncArray):
    values : List[Byte2] = json_list("values", Byte2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "byte2"


@json_model("byte3[]", Member)
class Array_Byte3(SyncArray):
    values : List[Byte3] = json_list("values", Byte3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "byte3"


@json_model("byte4[]", Member)
class Array_Byte4(SyncArray):
    values : List[Byte4] = json_list("values", Byte4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "byte4"


@json_model("sbyte2[]", Member)
class Array_Sbyte2(SyncArray):
    values : List[SByte2] = json_list("values", SByte2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "sbyte2"


@json_model("sbyte3[]", Member)
class Array_Sbyte3(SyncArray):
    values : List[SByte3] = json_list("values", SByte3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "sbyte3"


@json_model("sbyte4[]", Member)
class Array_Sbyte4(SyncArray):
    values : List[SByte4] = json_list("values", SByte4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "sbyte4"


@json_model("ushort2[]", Member)
class Array_Ushort2(SyncArray):
    values : List[UShort2] = json_list("values", UShort2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "ushort2"


@json_model("ushort3[]", Member)
class Array_Ushort3(SyncArray):
    values : List[UShort3] = json_list("values", UShort3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "ushort3"


@json_model("ushort4[]", Member)
class Array_Ushort4(SyncArray):
    values : List[UShort4] = json_list("values", UShort4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "ushort4"


@json_model("short2[]", Member)
class Array_Short2(SyncArray):
    values : List[Short2] = json_list("values", Short2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "short2"


@json_model("short3[]", Member)
class Array_Short3(SyncArray):
    values : List[Short3] = json_list("values", Short3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "short3"


@json_model("short4[]", Member)
class Array_Short4(SyncArray):
    values : List[Short4] = json_list("values", Short4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "short4"


@json_model("uint2[]", Member)
class Array_Uint2(SyncArray):
    values : List[UInt2] = json_list("values", UInt2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "uint2"


@json_model("uint3[]", Member)
class Array_Uint3(SyncArray):
    values : List[UInt3] = json_list("values", UInt3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "uint3"


@json_model("uint4[]", Member)
class Array_Uint4(SyncArray):
    values : List[UInt4] = json_list("values", UInt4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "uint4"


@json_model("int2[]", Member)
class Array_Int2(SyncArray):
    values : List[Int2] = json_list("values", Int2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "int2"


@json_model("int3[]", Member)
class Array_Int3(SyncArray):
    values : List[Int3] = json_list("values", Int3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "int3"


@json_model("int4[]", Member)
class Array_Int4(SyncArray):
    values : List[Int4] = json_list("values", Int4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "int4"


@json_model("ulong2[]", Member)
class Array_Ulong2(SyncArray):
    values : List[ULong2] = json_list("values", ULong2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "ulong2"


@json_model("ulong3[]", Member)
class Array_Ulong3(SyncArray):
    values : List[ULong3] = json_list("values", ULong3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "ulong3"


@json_model("ulong4[]", Member)
class Array_Ulong4(SyncArray):
    values : List[ULong4] = json_list("values", ULong4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "ulong4"


@json_model("long2[]", Member)
class Array_Long2(SyncArray):
    values : List[Long2] = json_list("values", Long2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "long2"


@json_model("long3[]", Member)
class Array_Long3(SyncArray):
    values : List[Long3] = json_list("values", Long3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "long3"


@json_model("long4[]", Member)
class Array_Long4(SyncArray):
    values : List[Long4] = json_list("values", Long4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "long4"


@json_model("float2[]", Member)
class Array_Float2(SyncArray):
    values : List[Float2] = json_list("values", Float2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "float2"


@json_model("float3[]", Member)
class Array_Float3(SyncArray):
    values : List[Float3] = json_list("values", Float3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "float3"


@json_model("float4[]", Member)
class Array_Float4(SyncArray):
    values : List[Float4] = json_list("values", Float4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "float4"


@json_model("double2[]", Member)
class Array_Double2(SyncArray):
    values : List[Double2] = json_list("values", Double2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "double2"


@json_model("double3[]", Member)
class Array_Double3(SyncArray):
    values : List[Double3] = json_list("values", Double3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "double3"


@json_model("double4[]", Member)
class Array_Double4(SyncArray):
    values : List[Double4] = json_list("values", Double4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "double4"


@json_model("float2x2[]", Member)
class Array_Float2x2(SyncArray):
    values : List[Float2x2] = json_list("values", Float2x2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "float2x2"


@json_model("float3x3[]", Member)
class Array_Float3x3(SyncArray):
    values : List[Float3x3] = json_list("values", Float3x3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "float3x3"


@json_model("float4x4[]", Member)
class Array_Float4x4(SyncArray):
    values : List[Float4x4] = json_list("values", Float4x4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "float4x4"


@json_model("double2x2[]", Member)
class Array_Double2x2(SyncArray):
    values : List[Double2x2] = json_list("values", Double2x2, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "double2x2"


@json_model("double3x3[]", Member)
class Array_Double3x3(SyncArray):
    values : List[Double3x3] = json_list("values", Double3x3, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "double3x3"


@json_model("double4x4[]", Member)
class Array_Double4x4(SyncArray):
    values : List[Double4x4] = json_list("values", Double4x4, default=MISSING)
    
    @property
    def element_type(self) -> str:
        return "double4x4"
