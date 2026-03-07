from dataclasses import dataclass
from decimal import Decimal
from typing import TypeAlias, Optional, Type, List, Dict
from decimal import Decimal
import numpy as np
import logging

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


def _make_first_char_uppercase(value : str) -> str:
    """
    Formats the string so that the first character is uppercase.

    Paramters
    ---------
    value : str
        The string to format.

    Returns
    -------
    The formatted string, the first char will now be uppercase (if it wasn't already).

    """
    if value and len(value) > 0:
        value = value[0].upper() + value[1:]
    
    return value


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
    type_name : str # The name of the Type in ResoniteLink.
    type : Type # The main type.
    type_code_name : str # The name of the main type as it appears in code.
    alt_type : Optional[Type] # A comatible alt type, if any. (This is used usually for python native types that are fully compatible with the corresponding numpy type).
    alt_type_code_name : Optional[str] # The name of the alt type as it appears in code.
    model_type_name : Optional[str]


type_mappings : Dict[str, LibraryTypeInfo] = { }

# 1. All non-model types need to be mapped manually
type_mappings.update({
    "bool": LibraryTypeInfo("Bool", t_bool, 't_bool', bool, 'bool', ""),
    
    "byte": LibraryTypeInfo("Byte", t_byte, 't_byte', int, 'int', ""),
    "sbyte": LibraryTypeInfo("SByte", t_sbyte, 't_sbyte', int, 'int', ""),
    "ushort": LibraryTypeInfo("UShort", t_ushort, 't_ushort', int, 'int', ""),
    "short": LibraryTypeInfo("Short", t_short, 't_short', int, 'int', ""),
    "uint": LibraryTypeInfo("UInt", t_uint, 't_uint', int, 'int', ""),
    "int": LibraryTypeInfo("Int", t_int, 't_int', int, 'int', ""),
    "ulong": LibraryTypeInfo("ULong", t_ulong, 't_ulong', int, 'int', ""),
    "long": LibraryTypeInfo("Long", t_long, 't_long', int, 'int', ""),
    
    "float": LibraryTypeInfo("Float", t_float, 't_float', float, 'float', ""),
    "double": LibraryTypeInfo("Double", t_double, 't_double', float, 'float', ""),
    
    "decimal": LibraryTypeInfo("Decimal", t_decimal, 't_decimal', None, None, ""),
    
    "char": LibraryTypeInfo("Char", str, 'str', None, None, ""),
    "string": LibraryTypeInfo("String", str, 'str', None, None, ""),
    "Uri": LibraryTypeInfo("Uri", str, 'str', None, None, ""),

    "DateTime": LibraryTypeInfo("DateTime", str, 'str', None, None, ""),
    "TimeSpan": LibraryTypeInfo("TimeSpan", str, 'str', None, None, "")
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
        type_mappings[primitive_type] = LibraryTypeInfo(_make_first_char_uppercase(primitive_type), model.data_class, model.data_class.__name__, None, None, model.type_name)


logger.debug(f"Registered types: [ {', '.join(type_mappings.keys())} ]")
