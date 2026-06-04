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
        yield f"from numpy.typing import NDArray\n"
        yield f"from typing import Union, Type, Tuple, List\n"
        yield f"\n"
        yield f"from resonitelink.types.aliases import *\n"
        yield f"from resonitelink.json import MISSING, json_model, json_element\n"
        yield f"from resonitelink.math import QuaternionBase\n"
        yield f"\n\n"

        yield f"__all__ = (\n"
        for quaternion_type in quaternion_types:
            type_info = type_mappings[quaternion_type]

            yield f"    '{type_info.type_name}Q',\n"
            
        yield f")\n"
        yield f"\n\n"

        def _generate_quaternion_class(model_name : str, class_name : str, element_type_code_name : str, element_alt_type_code_name : Optional[str]):
            yield f"@json_model(internal_type_name=\"t_{model_name}\")\n"
            yield f"class {class_name}(QuaternionBase[{element_type_code_name}]):\n"
            if element_alt_type_code_name:
                yield f"    w : Union[{element_type_code_name}, {element_alt_type_code_name}] = json_element(\"w\", {element_type_code_name}, default=MISSING)\n"
                yield f"    x : Union[{element_type_code_name}, {element_alt_type_code_name}] = json_element(\"x\", {element_type_code_name}, default=MISSING)\n"
                yield f"    y : Union[{element_type_code_name}, {element_alt_type_code_name}] = json_element(\"y\", {element_type_code_name}, default=MISSING)\n"
                yield f"    z : Union[{element_type_code_name}, {element_alt_type_code_name}] = json_element(\"z\", {element_type_code_name}, default=MISSING)\n"
            else:
                yield f"    w : {element_type_code_name} = json_element(\"w\", {element_type_code_name}, default=MISSING)\n"
                yield f"    x : {element_type_code_name} = json_element(\"x\", {element_type_code_name}, default=MISSING)\n"
                yield f"    y : {element_type_code_name} = json_element(\"y\", {element_type_code_name}, default=MISSING)\n"
                yield f"    z : {element_type_code_name} = json_element(\"z\", {element_type_code_name}, default=MISSING)\n"
            
            yield f"    \n"
            yield f"    @classmethod\n"
            yield f"    def _get_array_shape(cls) -> Tuple[int]:\n"
            yield f"        return (4,)\n"
            
            yield f"    \n"
            yield f"    @classmethod\n"
            yield f"    def _get_element_type(cls) -> Type[{element_type_code_name}]:\n"
            yield f"        return {element_type_code_name}\n"
            
            yield f"    \n"
            yield f"    @classmethod\n"
            yield f"    def _from_array(cls, array : NDArray[{element_type_code_name}]) -> '{class_name}':\n"
            yield f"        return cls(\n"
            yield f"            array[0],\n"
            yield f"            array[1],\n"
            yield f"            array[2],\n"
            yield f"            array[3],\n"
            yield f"        )\n"
            
            yield f"    \n"
            yield f"    def get_elements(self) -> List[{element_type_code_name}]:\n"
            yield f"        return [\n"
            yield f"            {element_type_code_name}(self.w),\n"
            yield f"            {element_type_code_name}(self.x),\n"
            yield f"            {element_type_code_name}(self.y),\n"
            yield f"            {element_type_code_name}(self.z),\n"
            yield f"        ]\n"

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
