from resonitelink.utils.types import type_mappings, quaternion_types
from resonitelink_codegen import CodeGenerator
from typing import Generator, Optional


class QuaternionsGenerator(CodeGenerator):
    """
    Generator for the quaternions.py model file.
    
    """
    def __init__(self):
        super().__init__("./resonitelink/models/datamodel/primitives/quaternions.py")
    
    def generate(self) -> Generator[str, None, None]:
        """
        Generates the content of quaternions.py

        """
        yield f"from resonitelink.types.aliases import *\n"
        yield f"from resonitelink.json import MISSING, json_model, json_element\n"
        yield f"\n\n"

        yield f"__all__ = (\n"
        for quaternion_type in quaternion_types:
            type_info = type_mappings[quaternion_type]

            yield f"    '{type_info.type_name}Q',\n"
            
        yield f")\n"
        yield f"\n\n"

        def _generate_quaternion_class(model_name : str, class_name : str, element_type_code_name : str, element_alt_type_code_name : Optional[str]):
            yield f"@json_model(internal_type_name=\"t_{model_name}\")\n"
            yield f"class {class_name}():\n"
            yield f"    x : {element_type_code_name} = json_element(\"x\", {element_type_code_name}, default=MISSING)\n"
            yield f"    y : {element_type_code_name} = json_element(\"y\", {element_type_code_name}, default=MISSING)\n"
            yield f"    z : {element_type_code_name} = json_element(\"z\", {element_type_code_name}, default=MISSING)\n"
            yield f"    w : {element_type_code_name} = json_element(\"w\", {element_type_code_name}, default=MISSING)\n"

        for quaternion_type in quaternion_types:
            type_info = type_mappings[quaternion_type]

            yield from _generate_quaternion_class(
                f"{quaternion_type}Q",
                f"{type_info.type_name}Q",
                type_info.type_code_name,
                type_info.alt_type_code_name
            )
            if quaternion_types.index(quaternion_type) < len(quaternion_types) - 1:
                yield f"\n\n"
