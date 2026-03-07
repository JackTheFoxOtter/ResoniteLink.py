from dataclasses import dataclass
from decimal import Decimal
from typing import TypeAlias, Optional, Type, List, Dict
from decimal import Decimal
import numpy as np
import logging

from resonitelink.utils import make_first_char_uppercase
from resonitelink.json import JSONModel


__all__ = (
    't_bool',
    't_byte',
    't_sbyte',
    't_ushort',
    't_short',
    't_uint',
    't_int',
    't_ulong',
    't_long',
    't_float',
    't_double',
    't_decimal',
    't_char',
    't_string',
    't_uri',
    't_datetime',
    't_timespan',
    'LibraryTypeInfo',
    'standalone_types',
    'vector_types',
    'quaternion_types',
    'matrix_types',
    'non_nullable_types',
    'enum_types',
    'primitive_types',
    'type_mappings',
)


logger = logging.getLogger("types")
logger.setLevel(logging.DEBUG)


# Type aliases for standalone types
t_bool : TypeAlias = np.bool
t_byte : TypeAlias = np.ubyte
t_sbyte : TypeAlias = np.byte
t_ushort : TypeAlias = np.uint16
t_short : TypeAlias = np.int16
t_uint : TypeAlias = np.uint32
t_int : TypeAlias = np.int32
t_ulong : TypeAlias = np.uint64
t_long : TypeAlias = np.int64
t_float : TypeAlias = np.float32
t_double : TypeAlias = np.float64
t_decimal : TypeAlias = Decimal
t_char : TypeAlias = str
t_string : TypeAlias = str
t_uri : TypeAlias = str
t_datetime : TypeAlias = str
t_timespan : TypeAlias = str


standalone_types = [
    "bool",

    "byte",
    "sbyte",
    "ushort",
    "short",
    "uint",
    "int",
    "ulong",
    "long",
    
    "float",
    "double",

    "decimal",
    
    "char",
    "string",
    "Uri",

    "DateTime",
    "TimeSpan",

    "color",
    "colorX",
    "color32"
]


vector_types = [
    "bool",

    "byte",
    "sbyte",
    "ushort",
    "short",
    "uint",
    "int",
    "ulong",
    "long",

    "float",
    "double"
]


quaternion_types = [
    "float",
    "double"
]


matrix_types = [
    "float",
    "double"
]


non_nullable_types = [
    "string",
    "Uri"
]


enum_types = [
    # TODO: All Enums
]


primitive_types : List[str] = [ ]

# 1. All primitives
primitive_types.extend(standalone_types)

# 2. All valid quaternions
for quaternion_type in quaternion_types:
    primitive_types.append(f"{quaternion_type}Q")

# 3. All valid vectors
for vector_type in vector_types:
    for dim in range(2, 5):
        primitive_types.append(f"{vector_type}{dim}")

# 4. All valid matrices
for matrix_type in matrix_types:
    for dim in range(2, 5):
        primitive_types.append(f"{matrix_type}{dim}x{dim}")


@dataclass(slots=True)
class LibraryTypeInfo():
    type_name : str
    type : Type # The "exact" type
    py_type : Optional[Type] # The equivalent Python standard type, if any
    model_type_name : Optional[str]


type_mappings : Dict[str, LibraryTypeInfo] = { }

# 1. All non-model types need to be mapped manually
type_mappings.update({
    "bool": LibraryTypeInfo("Bool", t_bool, bool, ""),
    
    "byte": LibraryTypeInfo("Byte", t_byte, int, ""),
    "sbyte": LibraryTypeInfo("SByte", t_sbyte, int, ""),
    "ushort": LibraryTypeInfo("UShort", t_ushort, int, ""),
    "short": LibraryTypeInfo("Short", t_short, int, ""),
    "uint": LibraryTypeInfo("UInt", t_uint, int, ""),
    "int": LibraryTypeInfo("Int", t_int, int, ""),
    "ulong": LibraryTypeInfo("ULong", t_ulong, int, ""),
    "long": LibraryTypeInfo("Long", t_long, int, ""),
    
    "float": LibraryTypeInfo("Float", t_float, float, ""),
    "double": LibraryTypeInfo("Double", t_double, float, ""),
    
    "decimal": LibraryTypeInfo("Decimal", t_decimal, None, ""),
    
    "char": LibraryTypeInfo("Char", str, str, ""),
    "string": LibraryTypeInfo("String", str, str, ""),
    "Uri": LibraryTypeInfo("Uri", str, str, ""),

    "DateTime": LibraryTypeInfo("DateTime", str, str, ""),
    "TimeSpan": LibraryTypeInfo("TimeSpan", str, str, "")
})

# 2. Now we can get the model for every remaining primitive type and add it
for primitive_type in primitive_types:
    if primitive_type in type_mappings.keys():
        # This will skip all primitive types that were already manually defined above
        continue

    try:
        # Try get the model for this primitive type
        model = JSONModel.find_model_internal(f"t_{primitive_type}")

    except KeyError:
        # Model not found!
        logger.warning(f"Missing model for primitive type '{primitive_type}'!")
    
    else:
        # Model found! Values are stored using its data class
        type_mappings[primitive_type] = LibraryTypeInfo(make_first_char_uppercase(primitive_type), model.data_class, None, model.type_name)


logger.debug(f"Registered types: [ {', '.join(type_mappings.keys())} ]")
