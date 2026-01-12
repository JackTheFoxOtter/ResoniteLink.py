#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#      >==============================================================================<
from resonitelink.models.datamodel.primitives import *
from resonitelink.models.datamodel import Field
from decimal import Decimal
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, Optional


@json_model("field_bool")
@dataclass(slots=True)
class Field_Bool(Field):
    value : Annotated[bool, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool"


@json_model("field_bool?")
@dataclass(slots=True)
class Field_Nullable_Bool(Field):
    value : Annotated[Optional[bool], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool"


@json_model("field_byte")
@dataclass(slots=True)
class Field_Byte(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte"


@json_model("field_byte?")
@dataclass(slots=True)
class Field_Nullable_Byte(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte"


@json_model("field_sbyte")
@dataclass(slots=True)
class Field_SByte(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte"


@json_model("field_sbyte?")
@dataclass(slots=True)
class Field_Nullable_SByte(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte"


@json_model("field_ushort")
@dataclass(slots=True)
class Field_UShort(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort"


@json_model("field_ushort?")
@dataclass(slots=True)
class Field_Nullable_UShort(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort"


@json_model("field_short")
@dataclass(slots=True)
class Field_Short(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short"


@json_model("field_short?")
@dataclass(slots=True)
class Field_Nullable_Short(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short"


@json_model("field_uint")
@dataclass(slots=True)
class Field_UInt(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint"


@json_model("field_uint?")
@dataclass(slots=True)
class Field_Nullable_UInt(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint"


@json_model("field_int")
@dataclass(slots=True)
class Field_Int(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int"


@json_model("field_int?")
@dataclass(slots=True)
class Field_Nullable_Int(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int"


@json_model("field_ulong")
@dataclass(slots=True)
class Field_ULong(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong"


@json_model("field_ulong?")
@dataclass(slots=True)
class Field_Nullable_ULong(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong"


@json_model("field_long")
@dataclass(slots=True)
class Field_Long(Field):
    value : Annotated[int, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long"


@json_model("field_long?")
@dataclass(slots=True)
class Field_Nullable_Long(Field):
    value : Annotated[Optional[int], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long"


@json_model("field_float")
@dataclass(slots=True)
class Field_Float(Field):
    value : Annotated[float, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float"


@json_model("field_float?")
@dataclass(slots=True)
class Field_Nullable_Float(Field):
    value : Annotated[Optional[float], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float"


@json_model("field_double")
@dataclass(slots=True)
class Field_Double(Field):
    value : Annotated[float, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double"


@json_model("field_double?")
@dataclass(slots=True)
class Field_Nullable_Double(Field):
    value : Annotated[Optional[float], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double"


@json_model("field_decimal")
@dataclass(slots=True)
class Field_Decimal(Field):
    value : Annotated[Decimal, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "decimal"


@json_model("field_decimal?")
@dataclass(slots=True)
class Field_Nullable_Decimal(Field):
    value : Annotated[Optional[Decimal], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "decimal"


@json_model("field_char")
@dataclass(slots=True)
class Field_Char(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "char"


@json_model("field_char?")
@dataclass(slots=True)
class Field_Nullable_Char(Field):
    value : Annotated[Optional[str], JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "char"


@json_model("field_string")
@dataclass(slots=True)
class Field_String(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "string"




@json_model("field_Uri")
@dataclass(slots=True)
class Field_Uri(Field):
    value : Annotated[str, JSONProperty("value")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "Uri"




@json_model("field_color")
@dataclass(slots=True)
class Field_Color(Field):
    value : Annotated[Color, JSONProperty("value", model_type_name="color")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color"


@json_model("field_color?")
@dataclass(slots=True)
class Field_Nullable_Color(Field):
    value : Annotated[Optional[Color], JSONProperty("value", model_type_name="color")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color"


@json_model("field_colorX")
@dataclass(slots=True)
class Field_ColorX(Field):
    value : Annotated[ColorX, JSONProperty("value", model_type_name="colorX")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "colorX"


@json_model("field_colorX?")
@dataclass(slots=True)
class Field_Nullable_ColorX(Field):
    value : Annotated[Optional[ColorX], JSONProperty("value", model_type_name="colorX")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "colorX"


@json_model("field_color32")
@dataclass(slots=True)
class Field_Color32(Field):
    value : Annotated[Color32, JSONProperty("value", model_type_name="color32")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color32"


@json_model("field_color32?")
@dataclass(slots=True)
class Field_Nullable_Color32(Field):
    value : Annotated[Optional[Color32], JSONProperty("value", model_type_name="color32")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "color32"


@json_model("field_floatQ")
@dataclass(slots=True)
class Field_FloatQ(Field):
    value : Annotated[FloatQ, JSONProperty("value", model_type_name="floatQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "floatQ"


@json_model("field_floatQ?")
@dataclass(slots=True)
class Field_Nullable_FloatQ(Field):
    value : Annotated[Optional[FloatQ], JSONProperty("value", model_type_name="floatQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "floatQ"


@json_model("field_doubleQ")
@dataclass(slots=True)
class Field_DoubleQ(Field):
    value : Annotated[DoubleQ, JSONProperty("value", model_type_name="doubleQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ"


@json_model("field_doubleQ?")
@dataclass(slots=True)
class Field_Nullable_DoubleQ(Field):
    value : Annotated[Optional[DoubleQ], JSONProperty("value", model_type_name="doubleQ")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ"


@json_model("field_bool2")
@dataclass(slots=True)
class Field_Bool2(Field):
    value : Annotated[Bool2, JSONProperty("value", model_type_name="bool2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool2"


@json_model("field_bool2?")
@dataclass(slots=True)
class Field_Nullable_Bool2(Field):
    value : Annotated[Optional[Bool2], JSONProperty("value", model_type_name="bool2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool2"


@json_model("field_bool3")
@dataclass(slots=True)
class Field_Bool3(Field):
    value : Annotated[Bool3, JSONProperty("value", model_type_name="bool3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool3"


@json_model("field_bool3?")
@dataclass(slots=True)
class Field_Nullable_Bool3(Field):
    value : Annotated[Optional[Bool3], JSONProperty("value", model_type_name="bool3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool3"


@json_model("field_bool4")
@dataclass(slots=True)
class Field_Bool4(Field):
    value : Annotated[Bool4, JSONProperty("value", model_type_name="bool4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool4"


@json_model("field_bool4?")
@dataclass(slots=True)
class Field_Nullable_Bool4(Field):
    value : Annotated[Optional[Bool4], JSONProperty("value", model_type_name="bool4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "bool4"


@json_model("field_byte2")
@dataclass(slots=True)
class Field_Byte2(Field):
    value : Annotated[Byte2, JSONProperty("value", model_type_name="byte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte2"


@json_model("field_byte2?")
@dataclass(slots=True)
class Field_Nullable_Byte2(Field):
    value : Annotated[Optional[Byte2], JSONProperty("value", model_type_name="byte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte2"


@json_model("field_byte3")
@dataclass(slots=True)
class Field_Byte3(Field):
    value : Annotated[Byte3, JSONProperty("value", model_type_name="byte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte3"


@json_model("field_byte3?")
@dataclass(slots=True)
class Field_Nullable_Byte3(Field):
    value : Annotated[Optional[Byte3], JSONProperty("value", model_type_name="byte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte3"


@json_model("field_byte4")
@dataclass(slots=True)
class Field_Byte4(Field):
    value : Annotated[Byte4, JSONProperty("value", model_type_name="byte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte4"


@json_model("field_byte4?")
@dataclass(slots=True)
class Field_Nullable_Byte4(Field):
    value : Annotated[Optional[Byte4], JSONProperty("value", model_type_name="byte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "byte4"


@json_model("field_sbyte2")
@dataclass(slots=True)
class Field_Sbyte2(Field):
    value : Annotated[SByte2, JSONProperty("value", model_type_name="sbyte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2"


@json_model("field_sbyte2?")
@dataclass(slots=True)
class Field_Nullable_Sbyte2(Field):
    value : Annotated[Optional[SByte2], JSONProperty("value", model_type_name="sbyte2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2"


@json_model("field_sbyte3")
@dataclass(slots=True)
class Field_Sbyte3(Field):
    value : Annotated[SByte3, JSONProperty("value", model_type_name="sbyte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3"


@json_model("field_sbyte3?")
@dataclass(slots=True)
class Field_Nullable_Sbyte3(Field):
    value : Annotated[Optional[SByte3], JSONProperty("value", model_type_name="sbyte3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3"


@json_model("field_sbyte4")
@dataclass(slots=True)
class Field_Sbyte4(Field):
    value : Annotated[SByte4, JSONProperty("value", model_type_name="sbyte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4"


@json_model("field_sbyte4?")
@dataclass(slots=True)
class Field_Nullable_Sbyte4(Field):
    value : Annotated[Optional[SByte4], JSONProperty("value", model_type_name="sbyte4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4"


@json_model("field_ushort2")
@dataclass(slots=True)
class Field_Ushort2(Field):
    value : Annotated[UShort2, JSONProperty("value", model_type_name="ushort2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort2"


@json_model("field_ushort2?")
@dataclass(slots=True)
class Field_Nullable_Ushort2(Field):
    value : Annotated[Optional[UShort2], JSONProperty("value", model_type_name="ushort2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort2"


@json_model("field_ushort3")
@dataclass(slots=True)
class Field_Ushort3(Field):
    value : Annotated[UShort3, JSONProperty("value", model_type_name="ushort3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort3"


@json_model("field_ushort3?")
@dataclass(slots=True)
class Field_Nullable_Ushort3(Field):
    value : Annotated[Optional[UShort3], JSONProperty("value", model_type_name="ushort3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort3"


@json_model("field_ushort4")
@dataclass(slots=True)
class Field_Ushort4(Field):
    value : Annotated[UShort4, JSONProperty("value", model_type_name="ushort4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort4"


@json_model("field_ushort4?")
@dataclass(slots=True)
class Field_Nullable_Ushort4(Field):
    value : Annotated[Optional[UShort4], JSONProperty("value", model_type_name="ushort4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ushort4"


@json_model("field_short2")
@dataclass(slots=True)
class Field_Short2(Field):
    value : Annotated[Short2, JSONProperty("value", model_type_name="short2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short2"


@json_model("field_short2?")
@dataclass(slots=True)
class Field_Nullable_Short2(Field):
    value : Annotated[Optional[Short2], JSONProperty("value", model_type_name="short2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short2"


@json_model("field_short3")
@dataclass(slots=True)
class Field_Short3(Field):
    value : Annotated[Short3, JSONProperty("value", model_type_name="short3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short3"


@json_model("field_short3?")
@dataclass(slots=True)
class Field_Nullable_Short3(Field):
    value : Annotated[Optional[Short3], JSONProperty("value", model_type_name="short3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short3"


@json_model("field_short4")
@dataclass(slots=True)
class Field_Short4(Field):
    value : Annotated[Short4, JSONProperty("value", model_type_name="short4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short4"


@json_model("field_short4?")
@dataclass(slots=True)
class Field_Nullable_Short4(Field):
    value : Annotated[Optional[Short4], JSONProperty("value", model_type_name="short4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "short4"


@json_model("field_uint2")
@dataclass(slots=True)
class Field_Uint2(Field):
    value : Annotated[UInt2, JSONProperty("value", model_type_name="uint2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint2"


@json_model("field_uint2?")
@dataclass(slots=True)
class Field_Nullable_Uint2(Field):
    value : Annotated[Optional[UInt2], JSONProperty("value", model_type_name="uint2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint2"


@json_model("field_uint3")
@dataclass(slots=True)
class Field_Uint3(Field):
    value : Annotated[UInt3, JSONProperty("value", model_type_name="uint3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint3"


@json_model("field_uint3?")
@dataclass(slots=True)
class Field_Nullable_Uint3(Field):
    value : Annotated[Optional[UInt3], JSONProperty("value", model_type_name="uint3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint3"


@json_model("field_uint4")
@dataclass(slots=True)
class Field_Uint4(Field):
    value : Annotated[UInt4, JSONProperty("value", model_type_name="uint4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint4"


@json_model("field_uint4?")
@dataclass(slots=True)
class Field_Nullable_Uint4(Field):
    value : Annotated[Optional[UInt4], JSONProperty("value", model_type_name="uint4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "uint4"


@json_model("field_int2")
@dataclass(slots=True)
class Field_Int2(Field):
    value : Annotated[Int2, JSONProperty("value", model_type_name="int2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int2"


@json_model("field_int2?")
@dataclass(slots=True)
class Field_Nullable_Int2(Field):
    value : Annotated[Optional[Int2], JSONProperty("value", model_type_name="int2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int2"


@json_model("field_int3")
@dataclass(slots=True)
class Field_Int3(Field):
    value : Annotated[Int3, JSONProperty("value", model_type_name="int3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int3"


@json_model("field_int3?")
@dataclass(slots=True)
class Field_Nullable_Int3(Field):
    value : Annotated[Optional[Int3], JSONProperty("value", model_type_name="int3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int3"


@json_model("field_int4")
@dataclass(slots=True)
class Field_Int4(Field):
    value : Annotated[Int4, JSONProperty("value", model_type_name="int4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int4"


@json_model("field_int4?")
@dataclass(slots=True)
class Field_Nullable_Int4(Field):
    value : Annotated[Optional[Int4], JSONProperty("value", model_type_name="int4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "int4"


@json_model("field_ulong2")
@dataclass(slots=True)
class Field_Ulong2(Field):
    value : Annotated[ULong2, JSONProperty("value", model_type_name="ulong2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong2"


@json_model("field_ulong2?")
@dataclass(slots=True)
class Field_Nullable_Ulong2(Field):
    value : Annotated[Optional[ULong2], JSONProperty("value", model_type_name="ulong2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong2"


@json_model("field_ulong3")
@dataclass(slots=True)
class Field_Ulong3(Field):
    value : Annotated[ULong3, JSONProperty("value", model_type_name="ulong3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong3"


@json_model("field_ulong3?")
@dataclass(slots=True)
class Field_Nullable_Ulong3(Field):
    value : Annotated[Optional[ULong3], JSONProperty("value", model_type_name="ulong3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong3"


@json_model("field_ulong4")
@dataclass(slots=True)
class Field_Ulong4(Field):
    value : Annotated[ULong4, JSONProperty("value", model_type_name="ulong4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong4"


@json_model("field_ulong4?")
@dataclass(slots=True)
class Field_Nullable_Ulong4(Field):
    value : Annotated[Optional[ULong4], JSONProperty("value", model_type_name="ulong4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "ulong4"


@json_model("field_long2")
@dataclass(slots=True)
class Field_Long2(Field):
    value : Annotated[Long2, JSONProperty("value", model_type_name="long2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long2"


@json_model("field_long2?")
@dataclass(slots=True)
class Field_Nullable_Long2(Field):
    value : Annotated[Optional[Long2], JSONProperty("value", model_type_name="long2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long2"


@json_model("field_long3")
@dataclass(slots=True)
class Field_Long3(Field):
    value : Annotated[Long3, JSONProperty("value", model_type_name="long3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long3"


@json_model("field_long3?")
@dataclass(slots=True)
class Field_Nullable_Long3(Field):
    value : Annotated[Optional[Long3], JSONProperty("value", model_type_name="long3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long3"


@json_model("field_long4")
@dataclass(slots=True)
class Field_Long4(Field):
    value : Annotated[Long4, JSONProperty("value", model_type_name="long4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long4"


@json_model("field_long4?")
@dataclass(slots=True)
class Field_Nullable_Long4(Field):
    value : Annotated[Optional[Long4], JSONProperty("value", model_type_name="long4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "long4"


@json_model("field_float2")
@dataclass(slots=True)
class Field_Float2(Field):
    value : Annotated[Float2, JSONProperty("value", model_type_name="float2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2"


@json_model("field_float2?")
@dataclass(slots=True)
class Field_Nullable_Float2(Field):
    value : Annotated[Optional[Float2], JSONProperty("value", model_type_name="float2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2"


@json_model("field_float3")
@dataclass(slots=True)
class Field_Float3(Field):
    value : Annotated[Float3, JSONProperty("value", model_type_name="float3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3"


@json_model("field_float3?")
@dataclass(slots=True)
class Field_Nullable_Float3(Field):
    value : Annotated[Optional[Float3], JSONProperty("value", model_type_name="float3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3"


@json_model("field_float4")
@dataclass(slots=True)
class Field_Float4(Field):
    value : Annotated[Float4, JSONProperty("value", model_type_name="float4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4"


@json_model("field_float4?")
@dataclass(slots=True)
class Field_Nullable_Float4(Field):
    value : Annotated[Optional[Float4], JSONProperty("value", model_type_name="float4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4"


@json_model("field_double2")
@dataclass(slots=True)
class Field_Double2(Field):
    value : Annotated[Double2, JSONProperty("value", model_type_name="double2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2"


@json_model("field_double2?")
@dataclass(slots=True)
class Field_Nullable_Double2(Field):
    value : Annotated[Optional[Double2], JSONProperty("value", model_type_name="double2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2"


@json_model("field_double3")
@dataclass(slots=True)
class Field_Double3(Field):
    value : Annotated[Double3, JSONProperty("value", model_type_name="double3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3"


@json_model("field_double3?")
@dataclass(slots=True)
class Field_Nullable_Double3(Field):
    value : Annotated[Optional[Double3], JSONProperty("value", model_type_name="double3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3"


@json_model("field_double4")
@dataclass(slots=True)
class Field_Double4(Field):
    value : Annotated[Double4, JSONProperty("value", model_type_name="double4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4"


@json_model("field_double4?")
@dataclass(slots=True)
class Field_Nullable_Double4(Field):
    value : Annotated[Optional[Double4], JSONProperty("value", model_type_name="double4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4"


@json_model("field_float2x2")
@dataclass(slots=True)
class Field_Float2x2(Field):
    value : Annotated[Float2x2, JSONProperty("value", model_type_name="float2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2x2"


@json_model("field_float2x2?")
@dataclass(slots=True)
class Field_Nullable_Float2x2(Field):
    value : Annotated[Optional[Float2x2], JSONProperty("value", model_type_name="float2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float2x2"


@json_model("field_float3x3")
@dataclass(slots=True)
class Field_Float3x3(Field):
    value : Annotated[Float3x3, JSONProperty("value", model_type_name="float3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3x3"


@json_model("field_float3x3?")
@dataclass(slots=True)
class Field_Nullable_Float3x3(Field):
    value : Annotated[Optional[Float3x3], JSONProperty("value", model_type_name="float3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float3x3"


@json_model("field_float4x4")
@dataclass(slots=True)
class Field_Float4x4(Field):
    value : Annotated[Float4x4, JSONProperty("value", model_type_name="float4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4x4"


@json_model("field_float4x4?")
@dataclass(slots=True)
class Field_Nullable_Float4x4(Field):
    value : Annotated[Optional[Float4x4], JSONProperty("value", model_type_name="float4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "float4x4"


@json_model("field_double2x2")
@dataclass(slots=True)
class Field_Double2x2(Field):
    value : Annotated[Double2x2, JSONProperty("value", model_type_name="double2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2x2"


@json_model("field_double2x2?")
@dataclass(slots=True)
class Field_Nullable_Double2x2(Field):
    value : Annotated[Optional[Double2x2], JSONProperty("value", model_type_name="double2x2")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double2x2"


@json_model("field_double3x3")
@dataclass(slots=True)
class Field_Double3x3(Field):
    value : Annotated[Double3x3, JSONProperty("value", model_type_name="double3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3x3"


@json_model("field_double3x3?")
@dataclass(slots=True)
class Field_Nullable_Double3x3(Field):
    value : Annotated[Optional[Double3x3], JSONProperty("value", model_type_name="double3x3")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double3x3"


@json_model("field_double4x4")
@dataclass(slots=True)
class Field_Double4x4(Field):
    value : Annotated[Double4x4, JSONProperty("value", model_type_name="double4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4x4"


@json_model("field_double4x4?")
@dataclass(slots=True)
class Field_Nullable_Double4x4(Field):
    value : Annotated[Optional[Double4x4], JSONProperty("value", model_type_name="double4x4")] = MISSING
    
    @property
    def value_type_name(self) -> str:
        return "double4x4"
