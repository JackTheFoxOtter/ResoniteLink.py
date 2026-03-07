from resonitelink.types import type_mappings, vector_types
from resonitelink_codegen import CodeGenerator
from typing import List, Generator, Optional


class VectorsGenerator(CodeGenerator):
    """
    Generator for the vectors.py model file.
    
    """
    def __init__(self):
        super().__init__("./resonitelink/models/datamodel/primitives/vectors.py")
    
    def generate(self) -> Generator[str, None, None]:
        """
        Generates the content of vectors.py

        """
        yield f"from resonitelink.types import *\n"
        yield f"from resonitelink.json import MISSING, json_model, json_element\n"
        yield f"from resonitelink.math import VectorBase\n"
        yield f"from numpy.typing import NDArray\n"
        yield f"from typing import Type, Tuple, List\n"
        yield f"\n\n"

        yield f"__all__ = (\n"
        for vector_type in vector_types:
            type_info = type_mappings[vector_type]

            yield f"    '{type_info.type_name}2',\n"
            yield f"    '{type_info.type_name}3',\n"
            yield f"    '{type_info.type_name}4',\n"
        
        yield f")\n"
        yield f"\n\n"

        def _generate_vector_class(model_name : str, class_name : str, element_type_code_name : str, element_alt_type_code_name : Optional[str], element_names : List[str]):
            yield f"@json_model(internal_type_name=\"t_{model_name}\")\n"
            yield f"class {class_name}(VectorBase[{element_type_code_name}]):\n"
            for element_name in element_names:
                if element_alt_type_code_name:
                    yield f"    {element_name} : Union[{element_type_code_name}, {element_alt_type_code_name}] = json_element(\"{element_name}\", {element_type_code_name}, default=MISSING)\n"
                else:
                    yield f"    {element_name} : {element_type_code_name} = json_element(\"{element_name}\", {element_type_code_name}, default=MISSING)\n"
            
            yield f"    \n"
            yield f"    @classmethod\n"
            yield f"    def _get_array_shape(cls) -> Tuple[int]:\n"
            yield f"        return ({len(element_names)},)\n"
            
            yield f"    \n"
            yield f"    @classmethod\n"
            yield f"    def _get_element_type(cls) -> Type[{element_type_code_name}]:\n"
            yield f"        return {element_type_code_name}\n"
            
            yield f"    \n"
            yield f"    @classmethod\n"
            yield f"    def _from_array(cls, array : NDArray[{element_type_code_name}]) -> '{class_name}':\n"
            yield f"        return cls(\n"
            for index, element_name in enumerate(element_names):
                yield f"            array[{index}],\n"
            yield f"        )\n"
            
            yield f"    \n"
            yield f"    def get_elements(self) -> List[{element_type_code_name}]:\n"
            yield f"        return [\n"
            for element_name in element_names:
                yield f"            {element_type_code_name}(self.{element_name}),\n"
            yield f"        ]\n"

        for vector_type in vector_types:
            type_info = type_mappings[vector_type]

            yield from _generate_vector_class(f"{vector_type}2", f"{type_info.type_name}2", type_info.type_code_name, type_info.alt_type_code_name, ["x", "y"])
            yield f"\n\n"
            yield from _generate_vector_class(f"{vector_type}3", f"{type_info.type_name}3", type_info.type_code_name, type_info.alt_type_code_name, ["x", "y", "z"])
            yield f"\n\n"
            yield from _generate_vector_class(f"{vector_type}4", f"{type_info.type_name}4", type_info.type_code_name, type_info.alt_type_code_name, ["x", "y", "z", "w"])
            if vector_types.index(vector_type) < len(vector_types) - 1:
                yield f"\n\n"
