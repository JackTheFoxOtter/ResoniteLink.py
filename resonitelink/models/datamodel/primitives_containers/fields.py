#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from decimal import Decimal
from typing import Optional

from resonitelink.models.datamodel.primitives import *
from resonitelink.models.datamodel import Member, Field
from resonitelink.types.aliases import *
from resonitelink.json import MISSING, json_model, json_element


__all__ = (
    'Field_Bool',
    'Field_Nullable_Bool',
    'Field_Byte',
    'Field_Nullable_Byte',
    'Field_SByte',
    'Field_Nullable_SByte',
    'Field_UShort',
    'Field_Nullable_UShort',
    'Field_Short',
    'Field_Nullable_Short',
    'Field_UInt',
    'Field_Nullable_UInt',
    'Field_Int',
    'Field_Nullable_Int',
    'Field_ULong',
    'Field_Nullable_ULong',
    'Field_Long',
    'Field_Nullable_Long',
    'Field_Float',
    'Field_Nullable_Float',
    'Field_Double',
    'Field_Nullable_Double',
    'Field_Decimal',
    'Field_Nullable_Decimal',
    'Field_Char',
    'Field_Nullable_Char',
    'Field_String',
    'Field_Uri',
    'Field_DateTime',
    'Field_Nullable_DateTime',
    'Field_TimeSpan',
    'Field_Nullable_TimeSpan',
    'Field_Color',
    'Field_Nullable_Color',
    'Field_ColorX',
    'Field_Nullable_ColorX',
    'Field_Color32',
    'Field_Nullable_Color32',
    'Field_FloatQ',
    'Field_Nullable_FloatQ',
    'Field_DoubleQ',
    'Field_Nullable_DoubleQ',
    'Field_Bool2',
    'Field_Nullable_Bool2',
    'Field_Bool3',
    'Field_Nullable_Bool3',
    'Field_Bool4',
    'Field_Nullable_Bool4',
    'Field_Byte2',
    'Field_Nullable_Byte2',
    'Field_Byte3',
    'Field_Nullable_Byte3',
    'Field_Byte4',
    'Field_Nullable_Byte4',
    'Field_Sbyte2',
    'Field_Nullable_Sbyte2',
    'Field_Sbyte3',
    'Field_Nullable_Sbyte3',
    'Field_Sbyte4',
    'Field_Nullable_Sbyte4',
    'Field_Ushort2',
    'Field_Nullable_Ushort2',
    'Field_Ushort3',
    'Field_Nullable_Ushort3',
    'Field_Ushort4',
    'Field_Nullable_Ushort4',
    'Field_Short2',
    'Field_Nullable_Short2',
    'Field_Short3',
    'Field_Nullable_Short3',
    'Field_Short4',
    'Field_Nullable_Short4',
    'Field_Uint2',
    'Field_Nullable_Uint2',
    'Field_Uint3',
    'Field_Nullable_Uint3',
    'Field_Uint4',
    'Field_Nullable_Uint4',
    'Field_Int2',
    'Field_Nullable_Int2',
    'Field_Int3',
    'Field_Nullable_Int3',
    'Field_Int4',
    'Field_Nullable_Int4',
    'Field_Ulong2',
    'Field_Nullable_Ulong2',
    'Field_Ulong3',
    'Field_Nullable_Ulong3',
    'Field_Ulong4',
    'Field_Nullable_Ulong4',
    'Field_Long2',
    'Field_Nullable_Long2',
    'Field_Long3',
    'Field_Nullable_Long3',
    'Field_Long4',
    'Field_Nullable_Long4',
    'Field_Float2',
    'Field_Nullable_Float2',
    'Field_Float3',
    'Field_Nullable_Float3',
    'Field_Float4',
    'Field_Nullable_Float4',
    'Field_Double2',
    'Field_Nullable_Double2',
    'Field_Double3',
    'Field_Nullable_Double3',
    'Field_Double4',
    'Field_Nullable_Double4',
    'Field_Float2x2',
    'Field_Nullable_Float2x2',
    'Field_Float3x3',
    'Field_Nullable_Float3x3',
    'Field_Float4x4',
    'Field_Nullable_Float4x4',
    'Field_Double2x2',
    'Field_Nullable_Double2x2',
    'Field_Double3x3',
    'Field_Nullable_Double3x3',
    'Field_Double4x4',
    'Field_Nullable_Double4x4',
)


@json_model("bool", Member)
class Field_Bool(Field):
    value : t_bool = json_element("value", t_bool, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "bool"


@json_model("bool?", Member)
class Field_Nullable_Bool(Field):
    value : Optional[t_bool] = json_element("value", t_bool, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "bool?"


@json_model("byte", Member)
class Field_Byte(Field):
    value : t_byte = json_element("value", t_byte, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "byte"


@json_model("byte?", Member)
class Field_Nullable_Byte(Field):
    value : Optional[t_byte] = json_element("value", t_byte, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "byte?"


@json_model("sbyte", Member)
class Field_SByte(Field):
    value : t_sbyte = json_element("value", t_sbyte, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte"


@json_model("sbyte?", Member)
class Field_Nullable_SByte(Field):
    value : Optional[t_sbyte] = json_element("value", t_sbyte, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte?"


@json_model("ushort", Member)
class Field_UShort(Field):
    value : t_ushort = json_element("value", t_ushort, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ushort"


@json_model("ushort?", Member)
class Field_Nullable_UShort(Field):
    value : Optional[t_ushort] = json_element("value", t_ushort, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ushort?"


@json_model("short", Member)
class Field_Short(Field):
    value : t_short = json_element("value", t_short, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "short"


@json_model("short?", Member)
class Field_Nullable_Short(Field):
    value : Optional[t_short] = json_element("value", t_short, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "short?"


@json_model("uint", Member)
class Field_UInt(Field):
    value : t_uint = json_element("value", t_uint, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "uint"


@json_model("uint?", Member)
class Field_Nullable_UInt(Field):
    value : Optional[t_uint] = json_element("value", t_uint, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "uint?"


@json_model("int", Member)
class Field_Int(Field):
    value : t_int = json_element("value", t_int, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "int"


@json_model("int?", Member)
class Field_Nullable_Int(Field):
    value : Optional[t_int] = json_element("value", t_int, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "int?"


@json_model("ulong", Member)
class Field_ULong(Field):
    value : t_ulong = json_element("value", t_ulong, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ulong"


@json_model("ulong?", Member)
class Field_Nullable_ULong(Field):
    value : Optional[t_ulong] = json_element("value", t_ulong, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ulong?"


@json_model("long", Member)
class Field_Long(Field):
    value : t_long = json_element("value", t_long, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "long"


@json_model("long?", Member)
class Field_Nullable_Long(Field):
    value : Optional[t_long] = json_element("value", t_long, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "long?"


@json_model("float", Member)
class Field_Float(Field):
    value : t_float = json_element("value", t_float, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float"


@json_model("float?", Member)
class Field_Nullable_Float(Field):
    value : Optional[t_float] = json_element("value", t_float, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float?"


@json_model("double", Member)
class Field_Double(Field):
    value : t_double = json_element("value", t_double, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double"


@json_model("double?", Member)
class Field_Nullable_Double(Field):
    value : Optional[t_double] = json_element("value", t_double, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double?"


@json_model("decimal", Member)
class Field_Decimal(Field):
    value : t_decimal = json_element("value", t_decimal, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "decimal"


@json_model("decimal?", Member)
class Field_Nullable_Decimal(Field):
    value : Optional[t_decimal] = json_element("value", t_decimal, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "decimal?"


@json_model("char", Member)
class Field_Char(Field):
    value : str = json_element("value", str, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "char"


@json_model("char?", Member)
class Field_Nullable_Char(Field):
    value : Optional[str] = json_element("value", str, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "char?"


@json_model("string", Member)
class Field_String(Field):
    value : str = json_element("value", str, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "string"




@json_model("Uri", Member)
class Field_Uri(Field):
    value : str = json_element("value", str, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "Uri"




@json_model("DateTime", Member)
class Field_DateTime(Field):
    value : str = json_element("value", str, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "DateTime"


@json_model("DateTime?", Member)
class Field_Nullable_DateTime(Field):
    value : Optional[str] = json_element("value", str, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "DateTime?"


@json_model("TimeSpan", Member)
class Field_TimeSpan(Field):
    value : str = json_element("value", str, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "TimeSpan"


@json_model("TimeSpan?", Member)
class Field_Nullable_TimeSpan(Field):
    value : Optional[str] = json_element("value", str, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "TimeSpan?"


@json_model("color", Member)
class Field_Color(Field):
    value : Color = json_element("value", Color, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "color"


@json_model("color?", Member)
class Field_Nullable_Color(Field):
    value : Optional[Color] = json_element("value", Color, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "color?"


@json_model("colorX", Member)
class Field_ColorX(Field):
    value : ColorX = json_element("value", ColorX, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "colorX"


@json_model("colorX?", Member)
class Field_Nullable_ColorX(Field):
    value : Optional[ColorX] = json_element("value", ColorX, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "colorX?"


@json_model("color32", Member)
class Field_Color32(Field):
    value : Color32 = json_element("value", Color32, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "color32"


@json_model("color32?", Member)
class Field_Nullable_Color32(Field):
    value : Optional[Color32] = json_element("value", Color32, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "color32?"


@json_model("floatQ", Member)
class Field_FloatQ(Field):
    value : FloatQ = json_element("value", FloatQ, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "floatQ"


@json_model("floatQ?", Member)
class Field_Nullable_FloatQ(Field):
    value : Optional[FloatQ] = json_element("value", FloatQ, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "floatQ?"


@json_model("doubleQ", Member)
class Field_DoubleQ(Field):
    value : DoubleQ = json_element("value", DoubleQ, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ"


@json_model("doubleQ?", Member)
class Field_Nullable_DoubleQ(Field):
    value : Optional[DoubleQ] = json_element("value", DoubleQ, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "doubleQ?"


@json_model("bool2", Member)
class Field_Bool2(Field):
    value : Bool2 = json_element("value", Bool2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "bool2"


@json_model("bool2?", Member)
class Field_Nullable_Bool2(Field):
    value : Optional[Bool2] = json_element("value", Bool2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "bool2?"


@json_model("bool3", Member)
class Field_Bool3(Field):
    value : Bool3 = json_element("value", Bool3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "bool3"


@json_model("bool3?", Member)
class Field_Nullable_Bool3(Field):
    value : Optional[Bool3] = json_element("value", Bool3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "bool3?"


@json_model("bool4", Member)
class Field_Bool4(Field):
    value : Bool4 = json_element("value", Bool4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "bool4"


@json_model("bool4?", Member)
class Field_Nullable_Bool4(Field):
    value : Optional[Bool4] = json_element("value", Bool4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "bool4?"


@json_model("byte2", Member)
class Field_Byte2(Field):
    value : Byte2 = json_element("value", Byte2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "byte2"


@json_model("byte2?", Member)
class Field_Nullable_Byte2(Field):
    value : Optional[Byte2] = json_element("value", Byte2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "byte2?"


@json_model("byte3", Member)
class Field_Byte3(Field):
    value : Byte3 = json_element("value", Byte3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "byte3"


@json_model("byte3?", Member)
class Field_Nullable_Byte3(Field):
    value : Optional[Byte3] = json_element("value", Byte3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "byte3?"


@json_model("byte4", Member)
class Field_Byte4(Field):
    value : Byte4 = json_element("value", Byte4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "byte4"


@json_model("byte4?", Member)
class Field_Nullable_Byte4(Field):
    value : Optional[Byte4] = json_element("value", Byte4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "byte4?"


@json_model("sbyte2", Member)
class Field_Sbyte2(Field):
    value : SByte2 = json_element("value", SByte2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2"


@json_model("sbyte2?", Member)
class Field_Nullable_Sbyte2(Field):
    value : Optional[SByte2] = json_element("value", SByte2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte2?"


@json_model("sbyte3", Member)
class Field_Sbyte3(Field):
    value : SByte3 = json_element("value", SByte3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3"


@json_model("sbyte3?", Member)
class Field_Nullable_Sbyte3(Field):
    value : Optional[SByte3] = json_element("value", SByte3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte3?"


@json_model("sbyte4", Member)
class Field_Sbyte4(Field):
    value : SByte4 = json_element("value", SByte4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4"


@json_model("sbyte4?", Member)
class Field_Nullable_Sbyte4(Field):
    value : Optional[SByte4] = json_element("value", SByte4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "sbyte4?"


@json_model("ushort2", Member)
class Field_Ushort2(Field):
    value : UShort2 = json_element("value", UShort2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ushort2"


@json_model("ushort2?", Member)
class Field_Nullable_Ushort2(Field):
    value : Optional[UShort2] = json_element("value", UShort2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ushort2?"


@json_model("ushort3", Member)
class Field_Ushort3(Field):
    value : UShort3 = json_element("value", UShort3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ushort3"


@json_model("ushort3?", Member)
class Field_Nullable_Ushort3(Field):
    value : Optional[UShort3] = json_element("value", UShort3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ushort3?"


@json_model("ushort4", Member)
class Field_Ushort4(Field):
    value : UShort4 = json_element("value", UShort4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ushort4"


@json_model("ushort4?", Member)
class Field_Nullable_Ushort4(Field):
    value : Optional[UShort4] = json_element("value", UShort4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ushort4?"


@json_model("short2", Member)
class Field_Short2(Field):
    value : Short2 = json_element("value", Short2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "short2"


@json_model("short2?", Member)
class Field_Nullable_Short2(Field):
    value : Optional[Short2] = json_element("value", Short2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "short2?"


@json_model("short3", Member)
class Field_Short3(Field):
    value : Short3 = json_element("value", Short3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "short3"


@json_model("short3?", Member)
class Field_Nullable_Short3(Field):
    value : Optional[Short3] = json_element("value", Short3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "short3?"


@json_model("short4", Member)
class Field_Short4(Field):
    value : Short4 = json_element("value", Short4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "short4"


@json_model("short4?", Member)
class Field_Nullable_Short4(Field):
    value : Optional[Short4] = json_element("value", Short4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "short4?"


@json_model("uint2", Member)
class Field_Uint2(Field):
    value : UInt2 = json_element("value", UInt2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "uint2"


@json_model("uint2?", Member)
class Field_Nullable_Uint2(Field):
    value : Optional[UInt2] = json_element("value", UInt2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "uint2?"


@json_model("uint3", Member)
class Field_Uint3(Field):
    value : UInt3 = json_element("value", UInt3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "uint3"


@json_model("uint3?", Member)
class Field_Nullable_Uint3(Field):
    value : Optional[UInt3] = json_element("value", UInt3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "uint3?"


@json_model("uint4", Member)
class Field_Uint4(Field):
    value : UInt4 = json_element("value", UInt4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "uint4"


@json_model("uint4?", Member)
class Field_Nullable_Uint4(Field):
    value : Optional[UInt4] = json_element("value", UInt4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "uint4?"


@json_model("int2", Member)
class Field_Int2(Field):
    value : Int2 = json_element("value", Int2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "int2"


@json_model("int2?", Member)
class Field_Nullable_Int2(Field):
    value : Optional[Int2] = json_element("value", Int2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "int2?"


@json_model("int3", Member)
class Field_Int3(Field):
    value : Int3 = json_element("value", Int3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "int3"


@json_model("int3?", Member)
class Field_Nullable_Int3(Field):
    value : Optional[Int3] = json_element("value", Int3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "int3?"


@json_model("int4", Member)
class Field_Int4(Field):
    value : Int4 = json_element("value", Int4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "int4"


@json_model("int4?", Member)
class Field_Nullable_Int4(Field):
    value : Optional[Int4] = json_element("value", Int4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "int4?"


@json_model("ulong2", Member)
class Field_Ulong2(Field):
    value : ULong2 = json_element("value", ULong2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ulong2"


@json_model("ulong2?", Member)
class Field_Nullable_Ulong2(Field):
    value : Optional[ULong2] = json_element("value", ULong2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ulong2?"


@json_model("ulong3", Member)
class Field_Ulong3(Field):
    value : ULong3 = json_element("value", ULong3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ulong3"


@json_model("ulong3?", Member)
class Field_Nullable_Ulong3(Field):
    value : Optional[ULong3] = json_element("value", ULong3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ulong3?"


@json_model("ulong4", Member)
class Field_Ulong4(Field):
    value : ULong4 = json_element("value", ULong4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ulong4"


@json_model("ulong4?", Member)
class Field_Nullable_Ulong4(Field):
    value : Optional[ULong4] = json_element("value", ULong4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "ulong4?"


@json_model("long2", Member)
class Field_Long2(Field):
    value : Long2 = json_element("value", Long2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "long2"


@json_model("long2?", Member)
class Field_Nullable_Long2(Field):
    value : Optional[Long2] = json_element("value", Long2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "long2?"


@json_model("long3", Member)
class Field_Long3(Field):
    value : Long3 = json_element("value", Long3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "long3"


@json_model("long3?", Member)
class Field_Nullable_Long3(Field):
    value : Optional[Long3] = json_element("value", Long3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "long3?"


@json_model("long4", Member)
class Field_Long4(Field):
    value : Long4 = json_element("value", Long4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "long4"


@json_model("long4?", Member)
class Field_Nullable_Long4(Field):
    value : Optional[Long4] = json_element("value", Long4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "long4?"


@json_model("float2", Member)
class Field_Float2(Field):
    value : Float2 = json_element("value", Float2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float2"


@json_model("float2?", Member)
class Field_Nullable_Float2(Field):
    value : Optional[Float2] = json_element("value", Float2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float2?"


@json_model("float3", Member)
class Field_Float3(Field):
    value : Float3 = json_element("value", Float3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float3"


@json_model("float3?", Member)
class Field_Nullable_Float3(Field):
    value : Optional[Float3] = json_element("value", Float3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float3?"


@json_model("float4", Member)
class Field_Float4(Field):
    value : Float4 = json_element("value", Float4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float4"


@json_model("float4?", Member)
class Field_Nullable_Float4(Field):
    value : Optional[Float4] = json_element("value", Float4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float4?"


@json_model("double2", Member)
class Field_Double2(Field):
    value : Double2 = json_element("value", Double2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double2"


@json_model("double2?", Member)
class Field_Nullable_Double2(Field):
    value : Optional[Double2] = json_element("value", Double2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double2?"


@json_model("double3", Member)
class Field_Double3(Field):
    value : Double3 = json_element("value", Double3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double3"


@json_model("double3?", Member)
class Field_Nullable_Double3(Field):
    value : Optional[Double3] = json_element("value", Double3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double3?"


@json_model("double4", Member)
class Field_Double4(Field):
    value : Double4 = json_element("value", Double4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double4"


@json_model("double4?", Member)
class Field_Nullable_Double4(Field):
    value : Optional[Double4] = json_element("value", Double4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double4?"


@json_model("float2x2", Member)
class Field_Float2x2(Field):
    value : Float2x2 = json_element("value", Float2x2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float2x2"


@json_model("float2x2?", Member)
class Field_Nullable_Float2x2(Field):
    value : Optional[Float2x2] = json_element("value", Float2x2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float2x2?"


@json_model("float3x3", Member)
class Field_Float3x3(Field):
    value : Float3x3 = json_element("value", Float3x3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float3x3"


@json_model("float3x3?", Member)
class Field_Nullable_Float3x3(Field):
    value : Optional[Float3x3] = json_element("value", Float3x3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float3x3?"


@json_model("float4x4", Member)
class Field_Float4x4(Field):
    value : Float4x4 = json_element("value", Float4x4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float4x4"


@json_model("float4x4?", Member)
class Field_Nullable_Float4x4(Field):
    value : Optional[Float4x4] = json_element("value", Float4x4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "float4x4?"


@json_model("double2x2", Member)
class Field_Double2x2(Field):
    value : Double2x2 = json_element("value", Double2x2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double2x2"


@json_model("double2x2?", Member)
class Field_Nullable_Double2x2(Field):
    value : Optional[Double2x2] = json_element("value", Double2x2, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double2x2?"


@json_model("double3x3", Member)
class Field_Double3x3(Field):
    value : Double3x3 = json_element("value", Double3x3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double3x3"


@json_model("double3x3?", Member)
class Field_Nullable_Double3x3(Field):
    value : Optional[Double3x3] = json_element("value", Double3x3, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double3x3?"


@json_model("double4x4", Member)
class Field_Double4x4(Field):
    value : Double4x4 = json_element("value", Double4x4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double4x4"


@json_model("double4x4?", Member)
class Field_Nullable_Double4x4(Field):
    value : Optional[Double4x4] = json_element("value", Double4x4, default=MISSING)
    
    @property
    def value_type_name(self) -> str:
        return "double4x4?"
