#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.models.datamodel.primitives import *
from resonitelink.models.datamodel import Field
from decimal import Decimal
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, Optional


@json_model("bool")
@dataclass(slots=True)
class Field_Bool(Field):
    value : Annotated[bool, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool"


@json_model("bool?")
@dataclass(slots=True)
class Field_Nullable_Bool(Field):
    value : Annotated[Optional[bool], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool?"


@json_model("byte")
@dataclass(slots=True)
class Field_Byte(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte"


@json_model("byte?")
@dataclass(slots=True)
class Field_Nullable_Byte(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte?"


@json_model("sbyte")
@dataclass(slots=True)
class Field_SByte(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte"


@json_model("sbyte?")
@dataclass(slots=True)
class Field_Nullable_SByte(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte?"


@json_model("ushort")
@dataclass(slots=True)
class Field_UShort(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort"


@json_model("ushort?")
@dataclass(slots=True)
class Field_Nullable_UShort(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort?"


@json_model("short")
@dataclass(slots=True)
class Field_Short(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short"


@json_model("short?")
@dataclass(slots=True)
class Field_Nullable_Short(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short?"


@json_model("uint")
@dataclass(slots=True)
class Field_UInt(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint"


@json_model("uint?")
@dataclass(slots=True)
class Field_Nullable_UInt(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint?"


@json_model("int")
@dataclass(slots=True)
class Field_Int(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int"


@json_model("int?")
@dataclass(slots=True)
class Field_Nullable_Int(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int?"


@json_model("ulong")
@dataclass(slots=True)
class Field_ULong(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong"


@json_model("ulong?")
@dataclass(slots=True)
class Field_Nullable_ULong(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong?"


@json_model("long")
@dataclass(slots=True)
class Field_Long(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long"


@json_model("long?")
@dataclass(slots=True)
class Field_Nullable_Long(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long?"


@json_model("float")
@dataclass(slots=True)
class Field_Float(Field):
    value : Annotated[float, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float"


@json_model("float?")
@dataclass(slots=True)
class Field_Nullable_Float(Field):
    value : Annotated[Optional[float], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float?"


@json_model("double")
@dataclass(slots=True)
class Field_Double(Field):
    value : Annotated[float, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double"


@json_model("double?")
@dataclass(slots=True)
class Field_Nullable_Double(Field):
    value : Annotated[Optional[float], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double?"


@json_model("decimal")
@dataclass(slots=True)
class Field_Decimal(Field):
    value : Annotated[Decimal, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "decimal"


@json_model("decimal?")
@dataclass(slots=True)
class Field_Nullable_Decimal(Field):
    value : Annotated[Optional[Decimal], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "decimal?"


@json_model("char")
@dataclass(slots=True)
class Field_Char(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "char"


@json_model("char?")
@dataclass(slots=True)
class Field_Nullable_Char(Field):
    value : Annotated[Optional[str], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "char?"


@json_model("string")
@dataclass(slots=True)
class Field_String(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "string"




@json_model("Uri")
@dataclass(slots=True)
class Field_Uri(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "Uri"




@json_model("DateTime")
@dataclass(slots=True)
class Field_DateTime(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "DateTime"


@json_model("DateTime?")
@dataclass(slots=True)
class Field_Nullable_DateTime(Field):
    value : Annotated[Optional[str], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "DateTime?"


@json_model("TimeSpan")
@dataclass(slots=True)
class Field_TimeSpan(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "TimeSpan"


@json_model("TimeSpan?")
@dataclass(slots=True)
class Field_Nullable_TimeSpan(Field):
    value : Annotated[Optional[str], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "TimeSpan?"


@json_model("color")
@dataclass(slots=True)
class Field_Color(Field):
    value : Annotated[Color, JSONProperty("value", model_type_name="t_color")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color"


@json_model("color?")
@dataclass(slots=True)
class Field_Nullable_Color(Field):
    value : Annotated[Optional[Color], JSONProperty("value", model_type_name="t_color")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color?"


@json_model("colorX")
@dataclass(slots=True)
class Field_ColorX(Field):
    value : Annotated[ColorX, JSONProperty("value", model_type_name="t_colorX")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "colorX"


@json_model("colorX?")
@dataclass(slots=True)
class Field_Nullable_ColorX(Field):
    value : Annotated[Optional[ColorX], JSONProperty("value", model_type_name="t_colorX")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "colorX?"


@json_model("color32")
@dataclass(slots=True)
class Field_Color32(Field):
    value : Annotated[Color32, JSONProperty("value", model_type_name="t_color32")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color32"


@json_model("color32?")
@dataclass(slots=True)
class Field_Nullable_Color32(Field):
    value : Annotated[Optional[Color32], JSONProperty("value", model_type_name="t_color32")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color32?"


@json_model("floatQ")
@dataclass(slots=True)
class Field_FloatQ(Field):
    value : Annotated[FloatQ, JSONProperty("value", model_type_name="t_floatQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "floatQ"


@json_model("floatQ?")
@dataclass(slots=True)
class Field_Nullable_FloatQ(Field):
    value : Annotated[Optional[FloatQ], JSONProperty("value", model_type_name="t_floatQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "floatQ?"


@json_model("doubleQ")
@dataclass(slots=True)
class Field_DoubleQ(Field):
    value : Annotated[DoubleQ, JSONProperty("value", model_type_name="t_doubleQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ"


@json_model("doubleQ?")
@dataclass(slots=True)
class Field_Nullable_DoubleQ(Field):
    value : Annotated[Optional[DoubleQ], JSONProperty("value", model_type_name="t_doubleQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ?"


@json_model("bool2")
@dataclass(slots=True)
class Field_Bool2(Field):
    value : Annotated[Bool2, JSONProperty("value", model_type_name="t_bool2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool2"


@json_model("bool2?")
@dataclass(slots=True)
class Field_Nullable_Bool2(Field):
    value : Annotated[Optional[Bool2], JSONProperty("value", model_type_name="t_bool2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool2?"


@json_model("bool3")
@dataclass(slots=True)
class Field_Bool3(Field):
    value : Annotated[Bool3, JSONProperty("value", model_type_name="t_bool3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool3"


@json_model("bool3?")
@dataclass(slots=True)
class Field_Nullable_Bool3(Field):
    value : Annotated[Optional[Bool3], JSONProperty("value", model_type_name="t_bool3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool3?"


@json_model("bool4")
@dataclass(slots=True)
class Field_Bool4(Field):
    value : Annotated[Bool4, JSONProperty("value", model_type_name="t_bool4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool4"


@json_model("bool4?")
@dataclass(slots=True)
class Field_Nullable_Bool4(Field):
    value : Annotated[Optional[Bool4], JSONProperty("value", model_type_name="t_bool4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool4?"


@json_model("byte2")
@dataclass(slots=True)
class Field_Byte2(Field):
    value : Annotated[Byte2, JSONProperty("value", model_type_name="t_byte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte2"


@json_model("byte2?")
@dataclass(slots=True)
class Field_Nullable_Byte2(Field):
    value : Annotated[Optional[Byte2], JSONProperty("value", model_type_name="t_byte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte2?"


@json_model("byte3")
@dataclass(slots=True)
class Field_Byte3(Field):
    value : Annotated[Byte3, JSONProperty("value", model_type_name="t_byte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte3"


@json_model("byte3?")
@dataclass(slots=True)
class Field_Nullable_Byte3(Field):
    value : Annotated[Optional[Byte3], JSONProperty("value", model_type_name="t_byte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte3?"


@json_model("byte4")
@dataclass(slots=True)
class Field_Byte4(Field):
    value : Annotated[Byte4, JSONProperty("value", model_type_name="t_byte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte4"


@json_model("byte4?")
@dataclass(slots=True)
class Field_Nullable_Byte4(Field):
    value : Annotated[Optional[Byte4], JSONProperty("value", model_type_name="t_byte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte4?"


@json_model("sbyte2")
@dataclass(slots=True)
class Field_Sbyte2(Field):
    value : Annotated[SByte2, JSONProperty("value", model_type_name="t_sbyte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2"


@json_model("sbyte2?")
@dataclass(slots=True)
class Field_Nullable_Sbyte2(Field):
    value : Annotated[Optional[SByte2], JSONProperty("value", model_type_name="t_sbyte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2?"


@json_model("sbyte3")
@dataclass(slots=True)
class Field_Sbyte3(Field):
    value : Annotated[SByte3, JSONProperty("value", model_type_name="t_sbyte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3"


@json_model("sbyte3?")
@dataclass(slots=True)
class Field_Nullable_Sbyte3(Field):
    value : Annotated[Optional[SByte3], JSONProperty("value", model_type_name="t_sbyte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3?"


@json_model("sbyte4")
@dataclass(slots=True)
class Field_Sbyte4(Field):
    value : Annotated[SByte4, JSONProperty("value", model_type_name="t_sbyte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4"


@json_model("sbyte4?")
@dataclass(slots=True)
class Field_Nullable_Sbyte4(Field):
    value : Annotated[Optional[SByte4], JSONProperty("value", model_type_name="t_sbyte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4?"


@json_model("ushort2")
@dataclass(slots=True)
class Field_Ushort2(Field):
    value : Annotated[UShort2, JSONProperty("value", model_type_name="t_ushort2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort2"


@json_model("ushort2?")
@dataclass(slots=True)
class Field_Nullable_Ushort2(Field):
    value : Annotated[Optional[UShort2], JSONProperty("value", model_type_name="t_ushort2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort2?"


@json_model("ushort3")
@dataclass(slots=True)
class Field_Ushort3(Field):
    value : Annotated[UShort3, JSONProperty("value", model_type_name="t_ushort3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort3"


@json_model("ushort3?")
@dataclass(slots=True)
class Field_Nullable_Ushort3(Field):
    value : Annotated[Optional[UShort3], JSONProperty("value", model_type_name="t_ushort3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort3?"


@json_model("ushort4")
@dataclass(slots=True)
class Field_Ushort4(Field):
    value : Annotated[UShort4, JSONProperty("value", model_type_name="t_ushort4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort4"


@json_model("ushort4?")
@dataclass(slots=True)
class Field_Nullable_Ushort4(Field):
    value : Annotated[Optional[UShort4], JSONProperty("value", model_type_name="t_ushort4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort4?"


@json_model("short2")
@dataclass(slots=True)
class Field_Short2(Field):
    value : Annotated[Short2, JSONProperty("value", model_type_name="t_short2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short2"


@json_model("short2?")
@dataclass(slots=True)
class Field_Nullable_Short2(Field):
    value : Annotated[Optional[Short2], JSONProperty("value", model_type_name="t_short2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short2?"


@json_model("short3")
@dataclass(slots=True)
class Field_Short3(Field):
    value : Annotated[Short3, JSONProperty("value", model_type_name="t_short3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short3"


@json_model("short3?")
@dataclass(slots=True)
class Field_Nullable_Short3(Field):
    value : Annotated[Optional[Short3], JSONProperty("value", model_type_name="t_short3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short3?"


@json_model("short4")
@dataclass(slots=True)
class Field_Short4(Field):
    value : Annotated[Short4, JSONProperty("value", model_type_name="t_short4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short4"


@json_model("short4?")
@dataclass(slots=True)
class Field_Nullable_Short4(Field):
    value : Annotated[Optional[Short4], JSONProperty("value", model_type_name="t_short4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short4?"


@json_model("uint2")
@dataclass(slots=True)
class Field_Uint2(Field):
    value : Annotated[UInt2, JSONProperty("value", model_type_name="t_uint2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint2"


@json_model("uint2?")
@dataclass(slots=True)
class Field_Nullable_Uint2(Field):
    value : Annotated[Optional[UInt2], JSONProperty("value", model_type_name="t_uint2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint2?"


@json_model("uint3")
@dataclass(slots=True)
class Field_Uint3(Field):
    value : Annotated[UInt3, JSONProperty("value", model_type_name="t_uint3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint3"


@json_model("uint3?")
@dataclass(slots=True)
class Field_Nullable_Uint3(Field):
    value : Annotated[Optional[UInt3], JSONProperty("value", model_type_name="t_uint3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint3?"


@json_model("uint4")
@dataclass(slots=True)
class Field_Uint4(Field):
    value : Annotated[UInt4, JSONProperty("value", model_type_name="t_uint4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint4"


@json_model("uint4?")
@dataclass(slots=True)
class Field_Nullable_Uint4(Field):
    value : Annotated[Optional[UInt4], JSONProperty("value", model_type_name="t_uint4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint4?"


@json_model("int2")
@dataclass(slots=True)
class Field_Int2(Field):
    value : Annotated[Int2, JSONProperty("value", model_type_name="t_int2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int2"


@json_model("int2?")
@dataclass(slots=True)
class Field_Nullable_Int2(Field):
    value : Annotated[Optional[Int2], JSONProperty("value", model_type_name="t_int2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int2?"


@json_model("int3")
@dataclass(slots=True)
class Field_Int3(Field):
    value : Annotated[Int3, JSONProperty("value", model_type_name="t_int3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int3"


@json_model("int3?")
@dataclass(slots=True)
class Field_Nullable_Int3(Field):
    value : Annotated[Optional[Int3], JSONProperty("value", model_type_name="t_int3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int3?"


@json_model("int4")
@dataclass(slots=True)
class Field_Int4(Field):
    value : Annotated[Int4, JSONProperty("value", model_type_name="t_int4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int4"


@json_model("int4?")
@dataclass(slots=True)
class Field_Nullable_Int4(Field):
    value : Annotated[Optional[Int4], JSONProperty("value", model_type_name="t_int4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int4?"


@json_model("ulong2")
@dataclass(slots=True)
class Field_Ulong2(Field):
    value : Annotated[ULong2, JSONProperty("value", model_type_name="t_ulong2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong2"


@json_model("ulong2?")
@dataclass(slots=True)
class Field_Nullable_Ulong2(Field):
    value : Annotated[Optional[ULong2], JSONProperty("value", model_type_name="t_ulong2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong2?"


@json_model("ulong3")
@dataclass(slots=True)
class Field_Ulong3(Field):
    value : Annotated[ULong3, JSONProperty("value", model_type_name="t_ulong3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong3"


@json_model("ulong3?")
@dataclass(slots=True)
class Field_Nullable_Ulong3(Field):
    value : Annotated[Optional[ULong3], JSONProperty("value", model_type_name="t_ulong3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong3?"


@json_model("ulong4")
@dataclass(slots=True)
class Field_Ulong4(Field):
    value : Annotated[ULong4, JSONProperty("value", model_type_name="t_ulong4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong4"


@json_model("ulong4?")
@dataclass(slots=True)
class Field_Nullable_Ulong4(Field):
    value : Annotated[Optional[ULong4], JSONProperty("value", model_type_name="t_ulong4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong4?"


@json_model("long2")
@dataclass(slots=True)
class Field_Long2(Field):
    value : Annotated[Long2, JSONProperty("value", model_type_name="t_long2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long2"


@json_model("long2?")
@dataclass(slots=True)
class Field_Nullable_Long2(Field):
    value : Annotated[Optional[Long2], JSONProperty("value", model_type_name="t_long2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long2?"


@json_model("long3")
@dataclass(slots=True)
class Field_Long3(Field):
    value : Annotated[Long3, JSONProperty("value", model_type_name="t_long3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long3"


@json_model("long3?")
@dataclass(slots=True)
class Field_Nullable_Long3(Field):
    value : Annotated[Optional[Long3], JSONProperty("value", model_type_name="t_long3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long3?"


@json_model("long4")
@dataclass(slots=True)
class Field_Long4(Field):
    value : Annotated[Long4, JSONProperty("value", model_type_name="t_long4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long4"


@json_model("long4?")
@dataclass(slots=True)
class Field_Nullable_Long4(Field):
    value : Annotated[Optional[Long4], JSONProperty("value", model_type_name="t_long4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long4?"


@json_model("float2")
@dataclass(slots=True)
class Field_Float2(Field):
    value : Annotated[Float2, JSONProperty("value", model_type_name="t_float2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2"


@json_model("float2?")
@dataclass(slots=True)
class Field_Nullable_Float2(Field):
    value : Annotated[Optional[Float2], JSONProperty("value", model_type_name="t_float2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2?"


@json_model("float3")
@dataclass(slots=True)
class Field_Float3(Field):
    value : Annotated[Float3, JSONProperty("value", model_type_name="t_float3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3"


@json_model("float3?")
@dataclass(slots=True)
class Field_Nullable_Float3(Field):
    value : Annotated[Optional[Float3], JSONProperty("value", model_type_name="t_float3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3?"


@json_model("float4")
@dataclass(slots=True)
class Field_Float4(Field):
    value : Annotated[Float4, JSONProperty("value", model_type_name="t_float4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4"


@json_model("float4?")
@dataclass(slots=True)
class Field_Nullable_Float4(Field):
    value : Annotated[Optional[Float4], JSONProperty("value", model_type_name="t_float4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4?"


@json_model("double2")
@dataclass(slots=True)
class Field_Double2(Field):
    value : Annotated[Double2, JSONProperty("value", model_type_name="t_double2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2"


@json_model("double2?")
@dataclass(slots=True)
class Field_Nullable_Double2(Field):
    value : Annotated[Optional[Double2], JSONProperty("value", model_type_name="t_double2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2?"


@json_model("double3")
@dataclass(slots=True)
class Field_Double3(Field):
    value : Annotated[Double3, JSONProperty("value", model_type_name="t_double3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3"


@json_model("double3?")
@dataclass(slots=True)
class Field_Nullable_Double3(Field):
    value : Annotated[Optional[Double3], JSONProperty("value", model_type_name="t_double3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3?"


@json_model("double4")
@dataclass(slots=True)
class Field_Double4(Field):
    value : Annotated[Double4, JSONProperty("value", model_type_name="t_double4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4"


@json_model("double4?")
@dataclass(slots=True)
class Field_Nullable_Double4(Field):
    value : Annotated[Optional[Double4], JSONProperty("value", model_type_name="t_double4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4?"


@json_model("float2x2")
@dataclass(slots=True)
class Field_Float2x2(Field):
    value : Annotated[Float2x2, JSONProperty("value", model_type_name="t_float2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2x2"


@json_model("float2x2?")
@dataclass(slots=True)
class Field_Nullable_Float2x2(Field):
    value : Annotated[Optional[Float2x2], JSONProperty("value", model_type_name="t_float2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2x2?"


@json_model("float3x3")
@dataclass(slots=True)
class Field_Float3x3(Field):
    value : Annotated[Float3x3, JSONProperty("value", model_type_name="t_float3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3x3"


@json_model("float3x3?")
@dataclass(slots=True)
class Field_Nullable_Float3x3(Field):
    value : Annotated[Optional[Float3x3], JSONProperty("value", model_type_name="t_float3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3x3?"


@json_model("float4x4")
@dataclass(slots=True)
class Field_Float4x4(Field):
    value : Annotated[Float4x4, JSONProperty("value", model_type_name="t_float4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4x4"


@json_model("float4x4?")
@dataclass(slots=True)
class Field_Nullable_Float4x4(Field):
    value : Annotated[Optional[Float4x4], JSONProperty("value", model_type_name="t_float4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4x4?"


@json_model("double2x2")
@dataclass(slots=True)
class Field_Double2x2(Field):
    value : Annotated[Double2x2, JSONProperty("value", model_type_name="t_double2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2x2"


@json_model("double2x2?")
@dataclass(slots=True)
class Field_Nullable_Double2x2(Field):
    value : Annotated[Optional[Double2x2], JSONProperty("value", model_type_name="t_double2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2x2?"


@json_model("double3x3")
@dataclass(slots=True)
class Field_Double3x3(Field):
    value : Annotated[Double3x3, JSONProperty("value", model_type_name="t_double3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3x3"


@json_model("double3x3?")
@dataclass(slots=True)
class Field_Nullable_Double3x3(Field):
    value : Annotated[Optional[Double3x3], JSONProperty("value", model_type_name="t_double3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3x3?"


@json_model("double4x4")
@dataclass(slots=True)
class Field_Double4x4(Field):
    value : Annotated[Double4x4, JSONProperty("value", model_type_name="t_double4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4x4"


@json_model("double4x4?")
@dataclass(slots=True)
class Field_Nullable_Double4x4(Field):
    value : Annotated[Optional[Double4x4], JSONProperty("value", model_type_name="t_double4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4x4?"
