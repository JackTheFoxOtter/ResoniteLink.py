from resonitelink_codegen import CodeGenerator
from resonitelink.types.types import type_mappings, primitive_types, non_nullable_types
from typing import Generator


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
        yield f"from resonitelink.models.datamodel import Member, Field\n"
        yield f"from resonitelink.types import *\n"
        yield f"from resonitelink.json import MISSING, json_model, json_element\n"
        yield f"from decimal import Decimal\n"
        yield f"from typing import Optional\n"
        yield f"\n\n"

        yield f"__all__ = (\n"
        for primitive_type in primitive_types:
            type_info = type_mappings[primitive_type]

            yield f"    'Field_{type_info.type_name}',\n"
            if primitive_type not in non_nullable_types:
                yield f"    'Field_Nullable_{type_info.type_name}',\n"
            
        yield f")\n"
        yield f"\n\n"

        def _generate_field_class(model_name : str, class_name : str, value_type_code_name : str, value_type_name : str, nullable : bool):
            yield f"@json_model(\"{model_name}\", Member)\n"
            yield f"class {class_name}(Field):\n"
            type_hint_str = f"Optional[{value_type_code_name}]" if nullable else f"{value_type_code_name}"
            json_prop_str = f"json_element(\"value\", {value_type_code_name}, default=MISSING)"
            yield f"    value : {type_hint_str} = {json_prop_str}\n"
            yield f"    \n"
            yield f"    @property\n"
            yield f"    def value_type_name(self) -> str:\n"
            yield f"        return \"{value_type_name}\"\n"

        for primitive_type in primitive_types:
            type_info = type_mappings[primitive_type]

            # 1. Non-Nullable fields
            yield from _generate_field_class(f"{primitive_type}", f"Field_{type_info.type_name}", type_info.type_code_name, f"{primitive_type}", False)
            yield f"\n\n"
            
            if primitive_type in non_nullable_types:
                # Skip generating nullable fields for non-nullable types
                if primitive_types.index(primitive_type) < len(primitive_types) - 1:
                    yield f"\n\n"
                continue
            
            # 2. Nullable fields
            yield from _generate_field_class(f"{primitive_type}?", f"Field_Nullable_{type_info.type_name}", type_info.type_code_name, f"{primitive_type}?", True)
            if primitive_types.index(primitive_type) < len(primitive_types) - 1:
                yield f"\n\n"
