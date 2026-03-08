#       >=============================================================================<
# NOTE: !!! THIS FILE IS AUTO-GENERATED! DO NOT EDIT! MODIFY CODEGENERATOR INSTEAD! !!!
#       >=============================================================================<
from numpy.typing import NDArray
from typing import Union, Type, Tuple, List

from resonitelink.types.aliases import *
from resonitelink.json import MISSING, json_model, json_element
from resonitelink.math import VectorBase


__all__ = (
    'Bool2',
    'Bool3',
    'Bool4',
    'Byte2',
    'Byte3',
    'Byte4',
    'SByte2',
    'SByte3',
    'SByte4',
    'UShort2',
    'UShort3',
    'UShort4',
    'Short2',
    'Short3',
    'Short4',
    'UInt2',
    'UInt3',
    'UInt4',
    'Int2',
    'Int3',
    'Int4',
    'ULong2',
    'ULong3',
    'ULong4',
    'Long2',
    'Long3',
    'Long4',
    'Float2',
    'Float3',
    'Float4',
    'Double2',
    'Double3',
    'Double4',
)


@json_model(internal_type_name="t_bool2")
class Bool2(VectorBase[t_bool]):
    x : Union[t_bool, bool] = json_element("x", t_bool, default=MISSING)
    y : Union[t_bool, bool] = json_element("y", t_bool, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_bool]:
        return t_bool
    
    @classmethod
    def _from_array(cls, array : NDArray[t_bool]) -> 'Bool2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_bool]:
        return [
            t_bool(self.x),
            t_bool(self.y),
        ]


@json_model(internal_type_name="t_bool3")
class Bool3(VectorBase[t_bool]):
    x : Union[t_bool, bool] = json_element("x", t_bool, default=MISSING)
    y : Union[t_bool, bool] = json_element("y", t_bool, default=MISSING)
    z : Union[t_bool, bool] = json_element("z", t_bool, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_bool]:
        return t_bool
    
    @classmethod
    def _from_array(cls, array : NDArray[t_bool]) -> 'Bool3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_bool]:
        return [
            t_bool(self.x),
            t_bool(self.y),
            t_bool(self.z),
        ]


@json_model(internal_type_name="t_bool4")
class Bool4(VectorBase[t_bool]):
    x : Union[t_bool, bool] = json_element("x", t_bool, default=MISSING)
    y : Union[t_bool, bool] = json_element("y", t_bool, default=MISSING)
    z : Union[t_bool, bool] = json_element("z", t_bool, default=MISSING)
    w : Union[t_bool, bool] = json_element("w", t_bool, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_bool]:
        return t_bool
    
    @classmethod
    def _from_array(cls, array : NDArray[t_bool]) -> 'Bool4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_bool]:
        return [
            t_bool(self.x),
            t_bool(self.y),
            t_bool(self.z),
            t_bool(self.w),
        ]


@json_model(internal_type_name="t_byte2")
class Byte2(VectorBase[t_byte]):
    x : Union[t_byte, int] = json_element("x", t_byte, default=MISSING)
    y : Union[t_byte, int] = json_element("y", t_byte, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_byte]:
        return t_byte
    
    @classmethod
    def _from_array(cls, array : NDArray[t_byte]) -> 'Byte2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_byte]:
        return [
            t_byte(self.x),
            t_byte(self.y),
        ]


@json_model(internal_type_name="t_byte3")
class Byte3(VectorBase[t_byte]):
    x : Union[t_byte, int] = json_element("x", t_byte, default=MISSING)
    y : Union[t_byte, int] = json_element("y", t_byte, default=MISSING)
    z : Union[t_byte, int] = json_element("z", t_byte, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_byte]:
        return t_byte
    
    @classmethod
    def _from_array(cls, array : NDArray[t_byte]) -> 'Byte3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_byte]:
        return [
            t_byte(self.x),
            t_byte(self.y),
            t_byte(self.z),
        ]


@json_model(internal_type_name="t_byte4")
class Byte4(VectorBase[t_byte]):
    x : Union[t_byte, int] = json_element("x", t_byte, default=MISSING)
    y : Union[t_byte, int] = json_element("y", t_byte, default=MISSING)
    z : Union[t_byte, int] = json_element("z", t_byte, default=MISSING)
    w : Union[t_byte, int] = json_element("w", t_byte, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_byte]:
        return t_byte
    
    @classmethod
    def _from_array(cls, array : NDArray[t_byte]) -> 'Byte4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_byte]:
        return [
            t_byte(self.x),
            t_byte(self.y),
            t_byte(self.z),
            t_byte(self.w),
        ]


@json_model(internal_type_name="t_sbyte2")
class SByte2(VectorBase[t_sbyte]):
    x : Union[t_sbyte, int] = json_element("x", t_sbyte, default=MISSING)
    y : Union[t_sbyte, int] = json_element("y", t_sbyte, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_sbyte]:
        return t_sbyte
    
    @classmethod
    def _from_array(cls, array : NDArray[t_sbyte]) -> 'SByte2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_sbyte]:
        return [
            t_sbyte(self.x),
            t_sbyte(self.y),
        ]


@json_model(internal_type_name="t_sbyte3")
class SByte3(VectorBase[t_sbyte]):
    x : Union[t_sbyte, int] = json_element("x", t_sbyte, default=MISSING)
    y : Union[t_sbyte, int] = json_element("y", t_sbyte, default=MISSING)
    z : Union[t_sbyte, int] = json_element("z", t_sbyte, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_sbyte]:
        return t_sbyte
    
    @classmethod
    def _from_array(cls, array : NDArray[t_sbyte]) -> 'SByte3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_sbyte]:
        return [
            t_sbyte(self.x),
            t_sbyte(self.y),
            t_sbyte(self.z),
        ]


@json_model(internal_type_name="t_sbyte4")
class SByte4(VectorBase[t_sbyte]):
    x : Union[t_sbyte, int] = json_element("x", t_sbyte, default=MISSING)
    y : Union[t_sbyte, int] = json_element("y", t_sbyte, default=MISSING)
    z : Union[t_sbyte, int] = json_element("z", t_sbyte, default=MISSING)
    w : Union[t_sbyte, int] = json_element("w", t_sbyte, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_sbyte]:
        return t_sbyte
    
    @classmethod
    def _from_array(cls, array : NDArray[t_sbyte]) -> 'SByte4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_sbyte]:
        return [
            t_sbyte(self.x),
            t_sbyte(self.y),
            t_sbyte(self.z),
            t_sbyte(self.w),
        ]


@json_model(internal_type_name="t_ushort2")
class UShort2(VectorBase[t_ushort]):
    x : Union[t_ushort, int] = json_element("x", t_ushort, default=MISSING)
    y : Union[t_ushort, int] = json_element("y", t_ushort, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_ushort]:
        return t_ushort
    
    @classmethod
    def _from_array(cls, array : NDArray[t_ushort]) -> 'UShort2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_ushort]:
        return [
            t_ushort(self.x),
            t_ushort(self.y),
        ]


@json_model(internal_type_name="t_ushort3")
class UShort3(VectorBase[t_ushort]):
    x : Union[t_ushort, int] = json_element("x", t_ushort, default=MISSING)
    y : Union[t_ushort, int] = json_element("y", t_ushort, default=MISSING)
    z : Union[t_ushort, int] = json_element("z", t_ushort, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_ushort]:
        return t_ushort
    
    @classmethod
    def _from_array(cls, array : NDArray[t_ushort]) -> 'UShort3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_ushort]:
        return [
            t_ushort(self.x),
            t_ushort(self.y),
            t_ushort(self.z),
        ]


@json_model(internal_type_name="t_ushort4")
class UShort4(VectorBase[t_ushort]):
    x : Union[t_ushort, int] = json_element("x", t_ushort, default=MISSING)
    y : Union[t_ushort, int] = json_element("y", t_ushort, default=MISSING)
    z : Union[t_ushort, int] = json_element("z", t_ushort, default=MISSING)
    w : Union[t_ushort, int] = json_element("w", t_ushort, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_ushort]:
        return t_ushort
    
    @classmethod
    def _from_array(cls, array : NDArray[t_ushort]) -> 'UShort4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_ushort]:
        return [
            t_ushort(self.x),
            t_ushort(self.y),
            t_ushort(self.z),
            t_ushort(self.w),
        ]


@json_model(internal_type_name="t_short2")
class Short2(VectorBase[t_short]):
    x : Union[t_short, int] = json_element("x", t_short, default=MISSING)
    y : Union[t_short, int] = json_element("y", t_short, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_short]:
        return t_short
    
    @classmethod
    def _from_array(cls, array : NDArray[t_short]) -> 'Short2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_short]:
        return [
            t_short(self.x),
            t_short(self.y),
        ]


@json_model(internal_type_name="t_short3")
class Short3(VectorBase[t_short]):
    x : Union[t_short, int] = json_element("x", t_short, default=MISSING)
    y : Union[t_short, int] = json_element("y", t_short, default=MISSING)
    z : Union[t_short, int] = json_element("z", t_short, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_short]:
        return t_short
    
    @classmethod
    def _from_array(cls, array : NDArray[t_short]) -> 'Short3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_short]:
        return [
            t_short(self.x),
            t_short(self.y),
            t_short(self.z),
        ]


@json_model(internal_type_name="t_short4")
class Short4(VectorBase[t_short]):
    x : Union[t_short, int] = json_element("x", t_short, default=MISSING)
    y : Union[t_short, int] = json_element("y", t_short, default=MISSING)
    z : Union[t_short, int] = json_element("z", t_short, default=MISSING)
    w : Union[t_short, int] = json_element("w", t_short, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_short]:
        return t_short
    
    @classmethod
    def _from_array(cls, array : NDArray[t_short]) -> 'Short4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_short]:
        return [
            t_short(self.x),
            t_short(self.y),
            t_short(self.z),
            t_short(self.w),
        ]


@json_model(internal_type_name="t_uint2")
class UInt2(VectorBase[t_uint]):
    x : Union[t_uint, int] = json_element("x", t_uint, default=MISSING)
    y : Union[t_uint, int] = json_element("y", t_uint, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_uint]:
        return t_uint
    
    @classmethod
    def _from_array(cls, array : NDArray[t_uint]) -> 'UInt2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_uint]:
        return [
            t_uint(self.x),
            t_uint(self.y),
        ]


@json_model(internal_type_name="t_uint3")
class UInt3(VectorBase[t_uint]):
    x : Union[t_uint, int] = json_element("x", t_uint, default=MISSING)
    y : Union[t_uint, int] = json_element("y", t_uint, default=MISSING)
    z : Union[t_uint, int] = json_element("z", t_uint, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_uint]:
        return t_uint
    
    @classmethod
    def _from_array(cls, array : NDArray[t_uint]) -> 'UInt3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_uint]:
        return [
            t_uint(self.x),
            t_uint(self.y),
            t_uint(self.z),
        ]


@json_model(internal_type_name="t_uint4")
class UInt4(VectorBase[t_uint]):
    x : Union[t_uint, int] = json_element("x", t_uint, default=MISSING)
    y : Union[t_uint, int] = json_element("y", t_uint, default=MISSING)
    z : Union[t_uint, int] = json_element("z", t_uint, default=MISSING)
    w : Union[t_uint, int] = json_element("w", t_uint, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_uint]:
        return t_uint
    
    @classmethod
    def _from_array(cls, array : NDArray[t_uint]) -> 'UInt4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_uint]:
        return [
            t_uint(self.x),
            t_uint(self.y),
            t_uint(self.z),
            t_uint(self.w),
        ]


@json_model(internal_type_name="t_int2")
class Int2(VectorBase[t_int]):
    x : Union[t_int, int] = json_element("x", t_int, default=MISSING)
    y : Union[t_int, int] = json_element("y", t_int, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_int]:
        return t_int
    
    @classmethod
    def _from_array(cls, array : NDArray[t_int]) -> 'Int2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_int]:
        return [
            t_int(self.x),
            t_int(self.y),
        ]


@json_model(internal_type_name="t_int3")
class Int3(VectorBase[t_int]):
    x : Union[t_int, int] = json_element("x", t_int, default=MISSING)
    y : Union[t_int, int] = json_element("y", t_int, default=MISSING)
    z : Union[t_int, int] = json_element("z", t_int, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_int]:
        return t_int
    
    @classmethod
    def _from_array(cls, array : NDArray[t_int]) -> 'Int3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_int]:
        return [
            t_int(self.x),
            t_int(self.y),
            t_int(self.z),
        ]


@json_model(internal_type_name="t_int4")
class Int4(VectorBase[t_int]):
    x : Union[t_int, int] = json_element("x", t_int, default=MISSING)
    y : Union[t_int, int] = json_element("y", t_int, default=MISSING)
    z : Union[t_int, int] = json_element("z", t_int, default=MISSING)
    w : Union[t_int, int] = json_element("w", t_int, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_int]:
        return t_int
    
    @classmethod
    def _from_array(cls, array : NDArray[t_int]) -> 'Int4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_int]:
        return [
            t_int(self.x),
            t_int(self.y),
            t_int(self.z),
            t_int(self.w),
        ]


@json_model(internal_type_name="t_ulong2")
class ULong2(VectorBase[t_ulong]):
    x : Union[t_ulong, int] = json_element("x", t_ulong, default=MISSING)
    y : Union[t_ulong, int] = json_element("y", t_ulong, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_ulong]:
        return t_ulong
    
    @classmethod
    def _from_array(cls, array : NDArray[t_ulong]) -> 'ULong2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_ulong]:
        return [
            t_ulong(self.x),
            t_ulong(self.y),
        ]


@json_model(internal_type_name="t_ulong3")
class ULong3(VectorBase[t_ulong]):
    x : Union[t_ulong, int] = json_element("x", t_ulong, default=MISSING)
    y : Union[t_ulong, int] = json_element("y", t_ulong, default=MISSING)
    z : Union[t_ulong, int] = json_element("z", t_ulong, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_ulong]:
        return t_ulong
    
    @classmethod
    def _from_array(cls, array : NDArray[t_ulong]) -> 'ULong3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_ulong]:
        return [
            t_ulong(self.x),
            t_ulong(self.y),
            t_ulong(self.z),
        ]


@json_model(internal_type_name="t_ulong4")
class ULong4(VectorBase[t_ulong]):
    x : Union[t_ulong, int] = json_element("x", t_ulong, default=MISSING)
    y : Union[t_ulong, int] = json_element("y", t_ulong, default=MISSING)
    z : Union[t_ulong, int] = json_element("z", t_ulong, default=MISSING)
    w : Union[t_ulong, int] = json_element("w", t_ulong, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_ulong]:
        return t_ulong
    
    @classmethod
    def _from_array(cls, array : NDArray[t_ulong]) -> 'ULong4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_ulong]:
        return [
            t_ulong(self.x),
            t_ulong(self.y),
            t_ulong(self.z),
            t_ulong(self.w),
        ]


@json_model(internal_type_name="t_long2")
class Long2(VectorBase[t_long]):
    x : Union[t_long, int] = json_element("x", t_long, default=MISSING)
    y : Union[t_long, int] = json_element("y", t_long, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_long]:
        return t_long
    
    @classmethod
    def _from_array(cls, array : NDArray[t_long]) -> 'Long2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_long]:
        return [
            t_long(self.x),
            t_long(self.y),
        ]


@json_model(internal_type_name="t_long3")
class Long3(VectorBase[t_long]):
    x : Union[t_long, int] = json_element("x", t_long, default=MISSING)
    y : Union[t_long, int] = json_element("y", t_long, default=MISSING)
    z : Union[t_long, int] = json_element("z", t_long, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_long]:
        return t_long
    
    @classmethod
    def _from_array(cls, array : NDArray[t_long]) -> 'Long3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_long]:
        return [
            t_long(self.x),
            t_long(self.y),
            t_long(self.z),
        ]


@json_model(internal_type_name="t_long4")
class Long4(VectorBase[t_long]):
    x : Union[t_long, int] = json_element("x", t_long, default=MISSING)
    y : Union[t_long, int] = json_element("y", t_long, default=MISSING)
    z : Union[t_long, int] = json_element("z", t_long, default=MISSING)
    w : Union[t_long, int] = json_element("w", t_long, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_long]:
        return t_long
    
    @classmethod
    def _from_array(cls, array : NDArray[t_long]) -> 'Long4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_long]:
        return [
            t_long(self.x),
            t_long(self.y),
            t_long(self.z),
            t_long(self.w),
        ]


@json_model(internal_type_name="t_float2")
class Float2(VectorBase[t_float]):
    x : Union[t_float, float] = json_element("x", t_float, default=MISSING)
    y : Union[t_float, float] = json_element("y", t_float, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_float]:
        return t_float
    
    @classmethod
    def _from_array(cls, array : NDArray[t_float]) -> 'Float2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_float]:
        return [
            t_float(self.x),
            t_float(self.y),
        ]


@json_model(internal_type_name="t_float3")
class Float3(VectorBase[t_float]):
    x : Union[t_float, float] = json_element("x", t_float, default=MISSING)
    y : Union[t_float, float] = json_element("y", t_float, default=MISSING)
    z : Union[t_float, float] = json_element("z", t_float, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_float]:
        return t_float
    
    @classmethod
    def _from_array(cls, array : NDArray[t_float]) -> 'Float3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_float]:
        return [
            t_float(self.x),
            t_float(self.y),
            t_float(self.z),
        ]


@json_model(internal_type_name="t_float4")
class Float4(VectorBase[t_float]):
    x : Union[t_float, float] = json_element("x", t_float, default=MISSING)
    y : Union[t_float, float] = json_element("y", t_float, default=MISSING)
    z : Union[t_float, float] = json_element("z", t_float, default=MISSING)
    w : Union[t_float, float] = json_element("w", t_float, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_float]:
        return t_float
    
    @classmethod
    def _from_array(cls, array : NDArray[t_float]) -> 'Float4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_float]:
        return [
            t_float(self.x),
            t_float(self.y),
            t_float(self.z),
            t_float(self.w),
        ]


@json_model(internal_type_name="t_double2")
class Double2(VectorBase[t_double]):
    x : Union[t_double, float] = json_element("x", t_double, default=MISSING)
    y : Union[t_double, float] = json_element("y", t_double, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (2,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_double]:
        return t_double
    
    @classmethod
    def _from_array(cls, array : NDArray[t_double]) -> 'Double2':
        return cls(
            array[0],
            array[1],
        )
    
    def get_elements(self) -> List[t_double]:
        return [
            t_double(self.x),
            t_double(self.y),
        ]


@json_model(internal_type_name="t_double3")
class Double3(VectorBase[t_double]):
    x : Union[t_double, float] = json_element("x", t_double, default=MISSING)
    y : Union[t_double, float] = json_element("y", t_double, default=MISSING)
    z : Union[t_double, float] = json_element("z", t_double, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (3,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_double]:
        return t_double
    
    @classmethod
    def _from_array(cls, array : NDArray[t_double]) -> 'Double3':
        return cls(
            array[0],
            array[1],
            array[2],
        )
    
    def get_elements(self) -> List[t_double]:
        return [
            t_double(self.x),
            t_double(self.y),
            t_double(self.z),
        ]


@json_model(internal_type_name="t_double4")
class Double4(VectorBase[t_double]):
    x : Union[t_double, float] = json_element("x", t_double, default=MISSING)
    y : Union[t_double, float] = json_element("y", t_double, default=MISSING)
    z : Union[t_double, float] = json_element("z", t_double, default=MISSING)
    w : Union[t_double, float] = json_element("w", t_double, default=MISSING)
    
    @classmethod
    def _get_array_shape(cls) -> Tuple[int]:
        return (4,)
    
    @classmethod
    def _get_element_type(cls) -> Type[t_double]:
        return t_double
    
    @classmethod
    def _from_array(cls, array : NDArray[t_double]) -> 'Double4':
        return cls(
            array[0],
            array[1],
            array[2],
            array[3],
        )
    
    def get_elements(self) -> List[t_double]:
        return [
            t_double(self.x),
            t_double(self.y),
            t_double(self.z),
            t_double(self.w),
        ]
