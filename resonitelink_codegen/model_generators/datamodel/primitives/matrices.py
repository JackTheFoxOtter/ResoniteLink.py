from resonitelink.utils.types import type_mappings, matrix_types
from resonitelink_codegen import CodeGenerator
from typing import List, Generator, Optional, Tuple


# TODO: There is a bug somewhere in the code generator, likely order of operations. Currently it won't run a second time.
#       It's most likely related to the additional imports.


class MatricesGenerator(CodeGenerator):
    """
    Generator for the matrices.py model file.
    
    """
    def __init__(self):
        super().__init__("./resonitelink/models/datamodel/primitives/matrices.py")
    
    def generate(self) -> Generator[str, None, None]:
        """
        Generates the content of matrices.py

        """
        yield f"from numpy.typing import NDArray\n"
        yield f"from typing import Union, Type, Tuple, List\n"
        yield f"\n"
        yield f"from resonitelink.types.aliases import *\n"
        yield f"from resonitelink.json import MISSING, json_model, json_element\n"
        yield f"from resonitelink.math import MatrixBase\n"
        yield f"\n\n"

        yield f"__all__ = (\n"
        for matrix_type in matrix_types:
            type_info = type_mappings[matrix_type]

            yield f"    '{type_info.type_name}2x2',\n"
            yield f"    '{type_info.type_name}3x3',\n"
            yield f"    '{type_info.type_name}4x4',\n"
            
        yield f")\n"
        yield f"\n\n"

        def _generate_matrix_class(model_name : str, class_name : str, element_type_code_name : str, element_alt_type_code_name : Optional[str], element_names : List[str], shape : Tuple[int, int]):
            yield f"@json_model(internal_type_name=\"t_{model_name}\")\n"
            yield f"class {class_name}(MatrixBase[{element_type_code_name}]):\n"
            for element_name in element_names:
                if element_alt_type_code_name:
                    yield f"    {element_name} : Union[{element_type_code_name}, {element_alt_type_code_name}] = json_element(\"{element_name}\", {element_type_code_name}, default=MISSING)\n"
                else:
                    yield f"    {element_name} : {element_type_code_name} = json_element(\"{element_name}\", {element_type_code_name}, default=MISSING)\n"
                
            yield f"    \n"
            yield f"    @classmethod\n"
            yield f"    def _get_array_shape(cls) -> Tuple[int, int]:\n"
            yield f"        return ({shape[0]},{shape[1]})\n"
            
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

        for matrix_type in matrix_types:
            type_info = type_mappings[matrix_type]

            yield from _generate_matrix_class(
                f"{matrix_type}2x2",
                f"{type_info.type_name}2x2",
                type_info.type_code_name,
                type_info.alt_type_code_name,
                [ "m00", "m01", "m10", "m11" ],
                (2,2)
            )
            yield f"\n\n"
            yield from _generate_matrix_class(
                f"{matrix_type}3x3",
                f"{type_info.type_name}3x3",
                type_info.type_code_name,
                type_info.alt_type_code_name,
                [ "m00", "m01", "m02", "m10", "m11", "m12", "m20", "m21", "m22" ],
                (3,3)
            )
            yield f"\n\n"
            yield from _generate_matrix_class(
                f"{matrix_type}4x4",
                f"{type_info.type_name}4x4",
                type_info.type_code_name,
                type_info.alt_type_code_name,
                [ "m00", "m01", "m02", "m03", "m10", "m11", "m12", "m13", "m20", "m21", "m22", "m23", "m30", "m31", "m32", "m33" ],
                (4,4)
            )
            if matrix_types.index(matrix_type) < len(matrix_types) - 1:
                yield f"\n\n"
