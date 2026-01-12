from resonitelink_codegen import CodeGenerator
from resonitelink.utils.types import type_mappings, primitive_types
from typing import Type, Generator


# NOTE: Reference output:
# from resonitelink.models.datamodel.primitives import *
# from resonitelink.models.datamodel.primitives_containers import *
# from resonitelink.models.datamodel.sync_array import SyncArray
# from decimal import Decimal
# from resonitelink.json import JSONProperty, json_model
# from dataclasses import dataclass
# from typing import Annotated, List

# @json_model("array_bool")
# @dataclass(slots=True)
# class Array_Bool(SyncArray):
#     values : Annotated[List[bool], JSONProperty("values")]
    
#     @property
#     def element_type(self) -> str:
#         return "bool"


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
        yield f"from resonitelink.models.datamodel.primitives_containers import *\n"
        yield f"from resonitelink.models.datamodel.sync_array import SyncArray\n"
        yield f"from decimal import Decimal\n"
        yield f"from resonitelink.json import JSONProperty, json_model\n"
        yield f"from dataclasses import dataclass\n"
        yield f"from typing import Annotated, List\n"
        yield f"\n\n"

        def _generate_array_class(model_name : str, class_name : str, value_type : Type, value_type_name : str):
            yield f"@json_model(\"{model_name}\")\n"
            yield f"@dataclass(slots=True)\n"
            yield f"class {class_name}(SyncArray):\n"
            yield f"    values : Annotated[List[{value_type.__name__}], JSONProperty(\"values\")]\n"
            yield f"    \n"
            yield f"    @property\n"
            yield f"    def value_type_name(self) -> str:\n"
            yield f"        return \"{value_type_name}\"\n"

        for primitive_type in primitive_types:
            type_info = type_mappings[primitive_type]

            yield from _generate_array_class(f"array_{primitive_type}", f"Array_{type_info.type_name}", type_info.type, primitive_type)
            if primitive_types.index(primitive_type) < len(primitive_types) - 1:
                yield f"\n\n"
