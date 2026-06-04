#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from numpy.typing import NDArray
from typing import Union, Type, Tuple, List

from resonitelink.types.aliases import *
from resonitelink.json import MISSING, json_model, json_element
from resonitelink.math import MatrixBase


__all__ = (
    'Float2x2',
    'Float3x3',
    'Float4x4',
    'Double2x2',
    'Double3x3',
    'Double4x4',
)


@json_model(internal_type_name="t_float2x2")
class Float2x2(MatrixBase[t_float]):
    m00 : Union[t_float, float] = json_element("m00", t_float, default=MISSING)
    m01 : Union[t_float, float] = json_element("m01", t_float, default=MISSING)
    m10 : Union[t_float, float] = json_element("m10", t_float, default=MISSING)
    m11 : Union[t_float, float] = json_element("m11", t_float, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int, int]:
        return (2,2)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_float]:
        return t_float
    
    @classmethod
    def _from_array(cls, array : NDArray[t_float]) -> 'Float2x2':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_float]:
        return [
            t_float(self.m00),
            t_float(self.m01),
            t_float(self.m10),
            t_float(self.m11),
        ]


@json_model(internal_type_name="t_float3x3")
class Float3x3(MatrixBase[t_float]):
    m00 : Union[t_float, float] = json_element("m00", t_float, default=MISSING)
    m01 : Union[t_float, float] = json_element("m01", t_float, default=MISSING)
    m02 : Union[t_float, float] = json_element("m02", t_float, default=MISSING)
    m10 : Union[t_float, float] = json_element("m10", t_float, default=MISSING)
    m11 : Union[t_float, float] = json_element("m11", t_float, default=MISSING)
    m12 : Union[t_float, float] = json_element("m12", t_float, default=MISSING)
    m20 : Union[t_float, float] = json_element("m20", t_float, default=MISSING)
    m21 : Union[t_float, float] = json_element("m21", t_float, default=MISSING)
    m22 : Union[t_float, float] = json_element("m22", t_float, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int, int]:
        return (3,3)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_float]:
        return t_float
    
    @classmethod
    def _from_array(cls, array : NDArray[t_float]) -> 'Float3x3':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
            array[4],
            array[5],
            array[6],
            array[7],
            array[8],
        )
    
    def get_elements(self) -> List[t_float]:
        return [
            t_float(self.m00),
            t_float(self.m01),
            t_float(self.m02),
            t_float(self.m10),
            t_float(self.m11),
            t_float(self.m12),
            t_float(self.m20),
            t_float(self.m21),
            t_float(self.m22),
        ]


@json_model(internal_type_name="t_float4x4")
class Float4x4(MatrixBase[t_float]):
    m00 : Union[t_float, float] = json_element("m00", t_float, default=MISSING)
    m01 : Union[t_float, float] = json_element("m01", t_float, default=MISSING)
    m02 : Union[t_float, float] = json_element("m02", t_float, default=MISSING)
    m03 : Union[t_float, float] = json_element("m03", t_float, default=MISSING)
    m10 : Union[t_float, float] = json_element("m10", t_float, default=MISSING)
    m11 : Union[t_float, float] = json_element("m11", t_float, default=MISSING)
    m12 : Union[t_float, float] = json_element("m12", t_float, default=MISSING)
    m13 : Union[t_float, float] = json_element("m13", t_float, default=MISSING)
    m20 : Union[t_float, float] = json_element("m20", t_float, default=MISSING)
    m21 : Union[t_float, float] = json_element("m21", t_float, default=MISSING)
    m22 : Union[t_float, float] = json_element("m22", t_float, default=MISSING)
    m23 : Union[t_float, float] = json_element("m23", t_float, default=MISSING)
    m30 : Union[t_float, float] = json_element("m30", t_float, default=MISSING)
    m31 : Union[t_float, float] = json_element("m31", t_float, default=MISSING)
    m32 : Union[t_float, float] = json_element("m32", t_float, default=MISSING)
    m33 : Union[t_float, float] = json_element("m33", t_float, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int, int]:
        return (4,4)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_float]:
        return t_float
    
    @classmethod
    def _from_array(cls, array : NDArray[t_float]) -> 'Float4x4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
            array[4],
            array[5],
            array[6],
            array[7],
            array[8],
            array[9],
            array[10],
            array[11],
            array[12],
            array[13],
            array[14],
            array[15],
        )
    
    def get_elements(self) -> List[t_float]:
        return [
            t_float(self.m00),
            t_float(self.m01),
            t_float(self.m02),
            t_float(self.m03),
            t_float(self.m10),
            t_float(self.m11),
            t_float(self.m12),
            t_float(self.m13),
            t_float(self.m20),
            t_float(self.m21),
            t_float(self.m22),
            t_float(self.m23),
            t_float(self.m30),
            t_float(self.m31),
            t_float(self.m32),
            t_float(self.m33),
        ]


@json_model(internal_type_name="t_double2x2")
class Double2x2(MatrixBase[t_double]):
    m00 : Union[t_double, float] = json_element("m00", t_double, default=MISSING)
    m01 : Union[t_double, float] = json_element("m01", t_double, default=MISSING)
    m10 : Union[t_double, float] = json_element("m10", t_double, default=MISSING)
    m11 : Union[t_double, float] = json_element("m11", t_double, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int, int]:
        return (2,2)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_double]:
        return t_double
    
    @classmethod
    def _from_array(cls, array : NDArray[t_double]) -> 'Double2x2':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_double]:
        return [
            t_double(self.m00),
            t_double(self.m01),
            t_double(self.m10),
            t_double(self.m11),
        ]


@json_model(internal_type_name="t_double3x3")
class Double3x3(MatrixBase[t_double]):
    m00 : Union[t_double, float] = json_element("m00", t_double, default=MISSING)
    m01 : Union[t_double, float] = json_element("m01", t_double, default=MISSING)
    m02 : Union[t_double, float] = json_element("m02", t_double, default=MISSING)
    m10 : Union[t_double, float] = json_element("m10", t_double, default=MISSING)
    m11 : Union[t_double, float] = json_element("m11", t_double, default=MISSING)
    m12 : Union[t_double, float] = json_element("m12", t_double, default=MISSING)
    m20 : Union[t_double, float] = json_element("m20", t_double, default=MISSING)
    m21 : Union[t_double, float] = json_element("m21", t_double, default=MISSING)
    m22 : Union[t_double, float] = json_element("m22", t_double, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int, int]:
        return (3,3)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_double]:
        return t_double
    
    @classmethod
    def _from_array(cls, array : NDArray[t_double]) -> 'Double3x3':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
            array[4],
            array[5],
            array[6],
            array[7],
            array[8],
        )
    
    def get_elements(self) -> List[t_double]:
        return [
            t_double(self.m00),
            t_double(self.m01),
            t_double(self.m02),
            t_double(self.m10),
            t_double(self.m11),
            t_double(self.m12),
            t_double(self.m20),
            t_double(self.m21),
            t_double(self.m22),
        ]


@json_model(internal_type_name="t_double4x4")
class Double4x4(MatrixBase[t_double]):
    m00 : Union[t_double, float] = json_element("m00", t_double, default=MISSING)
    m01 : Union[t_double, float] = json_element("m01", t_double, default=MISSING)
    m02 : Union[t_double, float] = json_element("m02", t_double, default=MISSING)
    m03 : Union[t_double, float] = json_element("m03", t_double, default=MISSING)
    m10 : Union[t_double, float] = json_element("m10", t_double, default=MISSING)
    m11 : Union[t_double, float] = json_element("m11", t_double, default=MISSING)
    m12 : Union[t_double, float] = json_element("m12", t_double, default=MISSING)
    m13 : Union[t_double, float] = json_element("m13", t_double, default=MISSING)
    m20 : Union[t_double, float] = json_element("m20", t_double, default=MISSING)
    m21 : Union[t_double, float] = json_element("m21", t_double, default=MISSING)
    m22 : Union[t_double, float] = json_element("m22", t_double, default=MISSING)
    m23 : Union[t_double, float] = json_element("m23", t_double, default=MISSING)
    m30 : Union[t_double, float] = json_element("m30", t_double, default=MISSING)
    m31 : Union[t_double, float] = json_element("m31", t_double, default=MISSING)
    m32 : Union[t_double, float] = json_element("m32", t_double, default=MISSING)
    m33 : Union[t_double, float] = json_element("m33", t_double, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int, int]:
        return (4,4)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_double]:
        return t_double
    
    @classmethod
    def _from_array(cls, array : NDArray[t_double]) -> 'Double4x4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
            array[4],
            array[5],
            array[6],
            array[7],
            array[8],
            array[9],
            array[10],
            array[11],
            array[12],
            array[13],
            array[14],
            array[15],
        )
    
    def get_elements(self) -> List[t_double]:
        return [
            t_double(self.m00),
            t_double(self.m01),
            t_double(self.m02),
            t_double(self.m03),
            t_double(self.m10),
            t_double(self.m11),
            t_double(self.m12),
            t_double(self.m13),
            t_double(self.m20),
            t_double(self.m21),
            t_double(self.m22),
            t_double(self.m23),
            t_double(self.m30),
            t_double(self.m31),
            t_double(self.m32),
            t_double(self.m33),
        ]
