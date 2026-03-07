from resonitelink_codegen import CodeGenerator
from resonitelink.types.types import type_mappings, primitive_types
from typing import Type, Generator


class ArraysGenerator(CodeGenerator):
    """
    Generator for the arrays.py model file.
    
    """
    def __init__(self):
        super().__init__("./resonitelink/models/datamodel/primitives_containers/arrays.py")
    
    def generate(self) -> Generator[str, None, None]:
        """
        Generates the content of arrays.py

        """
        yield f"from resonitelink.models.datamodel.primitives import *\n"
        yield f"from resonitelink.models.datamodel import Member, SyncArray\n"
        yield f"from resonitelink.json import MISSING, json_model, json_list\n"
        yield f"from decimal import Decimal\n"
        yield f"from typing import List\n"
        yield f"\n\n"

        yield f"__all__ = (\n"
        for vector_type in primitive_types:
            type_info = type_mappings[vector_type]

            yield f"    'Array_{type_info.type_name}',\n"
            
        yield f")\n"
        yield f"\n\n"

        def _generate_array_class(model_name : str, class_name : str, value_type : Type, value_type_name : str):
            yield f"@json_model(\"{model_name}\", Member)\n"
            yield f"class {class_name}(SyncArray):\n"
            yield f"    values : List[{value_type.__name__}] = json_list(\"values\", {value_type.__name__}, default=MISSING)\n"
            yield f"    \n"
            yield f"    @property\n"
            yield f"    def element_type(self) -> str:\n"
            yield f"        return \"{value_type_name}\"\n"

        for primitive_type in primitive_types:
            type_info = type_mappings[primitive_type]

            yield from _generate_array_class(f"{primitive_type}[]", f"Array_{type_info.type_name}", type_info.type, primitive_type)
            if primitive_types.index(primitive_type) < len(primitive_types) - 1:
                yield f"\n\n"
