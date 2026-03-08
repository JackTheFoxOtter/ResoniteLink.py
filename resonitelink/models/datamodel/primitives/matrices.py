#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.types.aliases import *
from resonitelink.json import MISSING, json_model, json_element


__all__ = (
    'Float2x2',
    'Float3x3',
    'Float4x4',
    'Double2x2',
    'Double3x3',
    'Double4x4',
)


@json_model(internal_type_name="t_float2x2")
class Float2x2():
    m00 : t_float = json_element("m00", t_float, default=MISSING)
    m01 : t_float = json_element("m01", t_float, default=MISSING)
    m10 : t_float = json_element("m10", t_float, default=MISSING)
    m11 : t_float = json_element("m11", t_float, default=MISSING)


@json_model(internal_type_name="t_float3x3")
class Float3x3():
    m00 : t_float = json_element("m00", t_float, default=MISSING)
    m01 : t_float = json_element("m01", t_float, default=MISSING)
    m02 : t_float = json_element("m02", t_float, default=MISSING)
    m10 : t_float = json_element("m10", t_float, default=MISSING)
    m11 : t_float = json_element("m11", t_float, default=MISSING)
    m12 : t_float = json_element("m12", t_float, default=MISSING)
    m20 : t_float = json_element("m20", t_float, default=MISSING)
    m21 : t_float = json_element("m21", t_float, default=MISSING)
    m22 : t_float = json_element("m22", t_float, default=MISSING)


@json_model(internal_type_name="t_float4x4")
class Float4x4():
    m00 : t_float = json_element("m00", t_float, default=MISSING)
    m01 : t_float = json_element("m01", t_float, default=MISSING)
    m02 : t_float = json_element("m02", t_float, default=MISSING)
    m03 : t_float = json_element("m03", t_float, default=MISSING)
    m10 : t_float = json_element("m10", t_float, default=MISSING)
    m11 : t_float = json_element("m11", t_float, default=MISSING)
    m12 : t_float = json_element("m12", t_float, default=MISSING)
    m13 : t_float = json_element("m13", t_float, default=MISSING)
    m20 : t_float = json_element("m20", t_float, default=MISSING)
    m21 : t_float = json_element("m21", t_float, default=MISSING)
    m22 : t_float = json_element("m22", t_float, default=MISSING)
    m23 : t_float = json_element("m23", t_float, default=MISSING)
    m30 : t_float = json_element("m30", t_float, default=MISSING)
    m31 : t_float = json_element("m31", t_float, default=MISSING)
    m32 : t_float = json_element("m32", t_float, default=MISSING)
    m33 : t_float = json_element("m33", t_float, default=MISSING)


@json_model(internal_type_name="t_double2x2")
class Double2x2():
    m00 : t_double = json_element("m00", t_double, default=MISSING)
    m01 : t_double = json_element("m01", t_double, default=MISSING)
    m10 : t_double = json_element("m10", t_double, default=MISSING)
    m11 : t_double = json_element("m11", t_double, default=MISSING)


@json_model(internal_type_name="t_double3x3")
class Double3x3():
    m00 : t_double = json_element("m00", t_double, default=MISSING)
    m01 : t_double = json_element("m01", t_double, default=MISSING)
    m02 : t_double = json_element("m02", t_double, default=MISSING)
    m10 : t_double = json_element("m10", t_double, default=MISSING)
    m11 : t_double = json_element("m11", t_double, default=MISSING)
    m12 : t_double = json_element("m12", t_double, default=MISSING)
    m20 : t_double = json_element("m20", t_double, default=MISSING)
    m21 : t_double = json_element("m21", t_double, default=MISSING)
    m22 : t_double = json_element("m22", t_double, default=MISSING)


@json_model(internal_type_name="t_double4x4")
class Double4x4():
    m00 : t_double = json_element("m00", t_double, default=MISSING)
    m01 : t_double = json_element("m01", t_double, default=MISSING)
    m02 : t_double = json_element("m02", t_double, default=MISSING)
    m03 : t_double = json_element("m03", t_double, default=MISSING)
    m10 : t_double = json_element("m10", t_double, default=MISSING)
    m11 : t_double = json_element("m11", t_double, default=MISSING)
    m12 : t_double = json_element("m12", t_double, default=MISSING)
    m13 : t_double = json_element("m13", t_double, default=MISSING)
    m20 : t_double = json_element("m20", t_double, default=MISSING)
    m21 : t_double = json_element("m21", t_double, default=MISSING)
    m22 : t_double = json_element("m22", t_double, default=MISSING)
    m23 : t_double = json_element("m23", t_double, default=MISSING)
    m30 : t_double = json_element("m30", t_double, default=MISSING)
    m31 : t_double = json_element("m31", t_double, default=MISSING)
    m32 : t_double = json_element("m32", t_double, default=MISSING)
    m33 : t_double = json_element("m33", t_double, default=MISSING)
