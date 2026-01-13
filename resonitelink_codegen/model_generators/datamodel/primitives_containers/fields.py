from resonitelink_codegen import CodeGenerator
from resonitelink.utils.types import type_mappings, primitive_types, non_nullable_types
from typing import Type, Generator


# NOTE: Reference output:
# from resonitelink.models.datamodel.primitives import *
# from resonitelink.models.datamodel import Field
# from decimal import Decimal
# from resonitelink.json import JSONProperty, json_model
# from dataclasses import dataclass
# from typing import Annotated, Optional

# @json_model("field_bool")
# @dataclass(slots=True)
# class Field_Bool(Field):
#     value : Annotated[bool, JSONProperty("value")]
    
#     @property
#     def value_type_name(self) -> str:
#         return "bool"


class FieldsGenerator(CodeGenerator):
    """
    Generator for the fields.py model file.
    
    """
    def __init__(self):
        super().__init__("./resonitelink/models/datamodel/primitives_containers/fields.py")
    
    def generate(self) -> Generator[str, None, None]:
        """
        Generates the content of fields.py

        """
        yield f"from resonitelink.models.datamodel.primitives import *\n"
        yield f"from resonitelink.models.datamodel import Field\n"
        yield f"from decimal import Decimal\n"
        yield f"from resonitelink.json import MISSING, JSONProperty, json_model\n"
        yield f"from dataclasses import dataclass\n"
        yield f"from typing import Annotated, Optional\n"
        yield f"\n\n"

        def _generate_field_class(model_name : str, class_name : str, value_type : Type, value_type_name : str, nullable : bool, model_type_name : str):
            yield f"@json_model(\"{model_name}\")\n"
            yield f"@dataclass(slots=True)\n"
            yield f"class {class_name}(Field):\n"
            type_hint_str = f"Optional[{value_type.__name__}]" if nullable else f"{value_type.__name__}"
            json_prop_str = f"JSONProperty(\"value\", model_type_name=\"{model_type_name}\")" if model_type_name else f"JSONProperty(\"value\")"
            yield f"    value : Annotated[{type_hint_str}, {json_prop_str}] = MISSING\n"
            yield f"    \n"
            yield f"    @property\n"
            yield f"    def value_type_name(self) -> str:\n"
            yield f"        return \"{value_type_name}\"\n"

        for primitive_type in primitive_types:
            type_info = type_mappings[primitive_type]

            # 1. Non-Nullable fields
            yield from _generate_field_class(f"{primitive_type}", f"Field_{type_info.type_name}", type_info.type, primitive_type, False, type_info.model_type_name)
            yield f"\n\n"
            
            if primitive_type in non_nullable_types:
                # Skip generating nullable fields for non-nullable types
                if primitive_types.index(primitive_type) < len(primitive_types) - 1:
                    yield f"\n\n"
                continue
            
            # 2. Nullable fields
            yield from _generate_field_class(f"{primitive_type}?", f"Field_Nullable_{type_info.type_name}", type_info.type, primitive_type, True, type_info.model_type_name)
            if primitive_types.index(primitive_type) < len(primitive_types) - 1:
                yield f"\n\n"
