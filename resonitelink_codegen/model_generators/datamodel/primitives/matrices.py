from resonitelink_codegen import CodeGenerator, type_mappings, matrix_types
from typing import Type, List, Generator


# NOTE: Reference output:
# from resonitelink.json import JSONProperty, json_model
# from dataclasses import dataclass
# from typing import Annotated

# @json_model("float2x2")
# @dataclass(slots=True)
# class Float2x2():
#     m00 : Annotated[float, JSONProperty("m00")]
#     m01 : Annotated[float, JSONProperty("m01")]
#     m10 : Annotated[float, JSONProperty("m10")]
#     m11 : Annotated[float, JSONProperty("m11")]


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
        yield f"from resonitelink.json import JSONProperty, json_model\n"
        yield f"from dataclasses import dataclass\n"
        yield f"from typing import Annotated\n"
        yield f"\n\n"

        def _generate_vector_class(model_name : str, class_name : str, element_type : Type, element_names : List[str]):
            yield f"@json_model(\"{model_name}\")\n"
            yield f"@dataclass(slots=True)\n"
            yield f"class {class_name}():\n"
            for element_name in element_names:
                yield f"    {element_name} : Annotated[{element_type.__name__}, JSONProperty(\"{element_name}\")]\n"

        for matrix_type in matrix_types:
            type_info = type_mappings[matrix_type]

            yield from _generate_vector_class(f"{matrix_type}2x2", f"{type_info.type_name}2x2", type_info.type, ["m00", "m01", "m10", "m11"])
            yield f"\n\n"
            yield from _generate_vector_class(f"{matrix_type}3x2", f"{type_info.type_name}3x3", type_info.type, ["m00", "m01", "m02", "m10", "m11", "m12", "m20", "m21", "m22"])
            yield f"\n\n"
            yield from _generate_vector_class(f"{matrix_type}4x4", f"{type_info.type_name}4x4", type_info.type, ["m00", "m01", "m02", "m03", "m10", "m11", "m12", "m13", "m20", "m21", "m22", "m23", "m30", "m31", "m32", "m33"])
            if matrix_types.index(matrix_type) < len(matrix_types) - 1:
                yield f"\n\n"
