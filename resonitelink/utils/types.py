from resonitelink.utils import make_first_char_uppercase
from resonitelink.json import JSONModel
from dataclasses import dataclass
from decimal import Decimal
from typing import Type, List, Dict
import logging


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
    type_name : str
    type : Type
    model_type_name : str


type_mappings : Dict[str, LibraryTypeInfo] = { }

# 1. All non-model types need to be mapped manually
type_mappings.update({
    "bool": LibraryTypeInfo("Bool", bool, ""),
    
    "byte": LibraryTypeInfo("Byte", int, ""),
    "sbyte": LibraryTypeInfo("SByte", int, ""),
    "ushort": LibraryTypeInfo("UShort", int, ""),
    "short": LibraryTypeInfo("Short", int, ""),
    "uint": LibraryTypeInfo("UInt", int, ""),
    "int": LibraryTypeInfo("Int", int, ""),
    "ulong": LibraryTypeInfo("ULong", int, ""),
    "long": LibraryTypeInfo("Long", int, ""),
    
    "float": LibraryTypeInfo("Float", float, ""),
    "double": LibraryTypeInfo("Double", float, ""),
    
    "decimal": LibraryTypeInfo("Decimal", Decimal, ""),
    
    "char": LibraryTypeInfo("Char", str, ""),
    "string": LibraryTypeInfo("String", str, ""),
    "Uri": LibraryTypeInfo("Uri", str, ""),

    "DateTime": LibraryTypeInfo("DateTime", str, ""),
    "TimeSpan": LibraryTypeInfo("TimeSpan", str, "") 
})

# 2. Now we can get the model for every remaining primitive type and add it
for primitive_type in primitive_types:
    if primitive_type in type_mappings.keys():
        # This will skip all primitive types that were already manually defined above
        continue

    try:
        # Try get the model for this primitive type
        model = JSONModel.get_for_type_name(f"t_{primitive_type}")

    except KeyError:
        # Model not found!
        logger.warning(f"Missing model for primitive type '{primitive_type}'!")
    
    else:
        # Model found! Values are stored using its data class
        type_mappings[primitive_type] = LibraryTypeInfo(make_first_char_uppercase(primitive_type), model.data_class, model.type_name)


logger.debug(f"Registered types: [ {', '.join(type_mappings.keys())} ]")


