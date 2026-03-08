from dataclasses import dataclass
from typing import Optional, Type, List, Dict
import logging

from resonitelink.utils.utils import make_first_char_uppercase
from resonitelink.types import *
from resonitelink.json import JSONModel


__all__ = (
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
        type_mappings[primitive_type] = LibraryTypeInfo(make_first_char_uppercase(primitive_type), model.data_class, model.data_class.__name__, None, None, model.type_name)


logger.debug(f"Registered types: [ {', '.join(type_mappings.keys())} ]")
