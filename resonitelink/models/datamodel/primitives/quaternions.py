#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from numpy.typing import NDArray
from typing import Union, Type, Tuple, List

from resonitelink.types.aliases import *
from resonitelink.json import MISSING, json_model, json_element
from resonitelink.math import QuaternionBase


__all__ = (
    'FloatQ',
    'DoubleQ',
)


@json_model(internal_type_name="t_floatQ")
class FloatQ(QuaternionBase[t_float]):
    w : Union[t_float, float] = json_element("w", t_float, default=MISSING)
    x : Union[t_float, float] = json_element("x", t_float, default=MISSING)
    y : Union[t_float, float] = json_element("y", t_float, default=MISSING)
    z : Union[t_float, float] = json_element("z", t_float, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_float]:
        return t_float
    
    @classmethod
    def _from_array(cls, array : NDArray[t_float]) -> 'FloatQ':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_float]:
        return [
            t_float(self.w),
            t_float(self.x),
            t_float(self.y),
            t_float(self.z),
        ]


@json_model(internal_type_name="t_doubleQ")
class DoubleQ(QuaternionBase[t_double]):
    w : Union[t_double, float] = json_element("w", t_double, default=MISSING)
    x : Union[t_double, float] = json_element("x", t_double, default=MISSING)
    y : Union[t_double, float] = json_element("y", t_double, default=MISSING)
    z : Union[t_double, float] = json_element("z", t_double, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_double]:
        return t_double
    
    @classmethod
    def _from_array(cls, array : NDArray[t_double]) -> 'DoubleQ':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_double]:
        return [
            t_double(self.w),
            t_double(self.x),
            t_double(self.y),
            t_double(self.z),
        ]
