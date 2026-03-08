#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from resonitelink.types.aliases import *
from resonitelink.json import MISSING, json_model, json_element


__all__ = (
    'FloatQ',
    'DoubleQ',
)


@json_model(internal_type_name="t_floatQ")
class FloatQ():
    x : t_float = json_element("x", t_float, default=MISSING)
    y : t_float = json_element("y", t_float, default=MISSING)
    z : t_float = json_element("z", t_float, default=MISSING)
    w : t_float = json_element("w", t_float, default=MISSING)


@json_model(internal_type_name="t_doubleQ")
class DoubleQ():
    x : t_double = json_element("x", t_double, default=MISSING)
    y : t_double = json_element("y", t_double, default=MISSING)
    z : t_double = json_element("z", t_double, default=MISSING)
    w : t_double = json_element("w", t_double, default=MISSING)
