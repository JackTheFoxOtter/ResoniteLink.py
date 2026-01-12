from resonitelink_codegen import CodeGenerator, type_mappings, vector_types
from typing import Type, List, Generator


# NOTE: Reference output:
# from resonitelink.json import JSONProperty, json_model
# from dataclasses import dataclass
# from typing import Annotated

# @json_model("int2")
# @dataclass(slots=True)
# class Vector_Int2():
#     x : Annotated[int, JSONProperty("x")]
#     y : Annotated[int, JSONProperty("y")]


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

        for vector_type in vector_types:
            type_info = type_mappings[vector_type]

            yield from _generate_vector_class(f"{vector_type}2", f"{type_info.type_name}2", type_info.type, ["x", "y"])
            yield f"\n\n"
            yield from _generate_vector_class(f"{vector_type}3", f"{type_info.type_name}3", type_info.type, ["x", "y", "z"])
            yield f"\n\n"
            yield from _generate_vector_class(f"{vector_type}4", f"{type_info.type_name}4", type_info.type, ["x", "y", "z", "w"])
            if vector_types.index(vector_type) < len(vector_types) - 1:
                yield f"\n\n"
