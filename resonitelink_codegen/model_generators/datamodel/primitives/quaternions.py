from resonitelink_codegen import CodeGenerator
from resonitelink.utils.types import type_mappings, quaternion_types
from typing import Type, Generator


# NOTE: Reference output:
# from resonitelink.json import JSONProperty, json_model
# from dataclasses import dataclass
# from typing import Annotated

# @json_model("floatQ")
# @dataclass(slots=True)
# class Quaternion_Float():
#     x : Annotated[float, JSONProperty("x")]
#     y : Annotated[float, JSONProperty("y")]
#     z : Annotated[float, JSONProperty("z")]
#     w : Annotated[float, JSONProperty("w")]


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
        yield f"from resonitelink.json import JSONProperty, json_model\n"
        yield f"from dataclasses import dataclass\n"
        yield f"from typing import Annotated\n"
        yield f"\n\n"

        def _generate_quaternion_class(model_name : str, class_name : str, element_type : Type):
            yield f"@json_model(\"{model_name}\")\n"
            yield f"@dataclass(slots=True)\n"
            yield f"class {class_name}():\n"
            yield f"    x : Annotated[{element_type.__name__}, JSONProperty(\"x\")]\n"
            yield f"    y : Annotated[{element_type.__name__}, JSONProperty(\"y\")]\n"
            yield f"    z : Annotated[{element_type.__name__}, JSONProperty(\"z\")]\n"
            yield f"    w : Annotated[{element_type.__name__}, JSONProperty(\"w\")]\n"

        for quaternion_type in quaternion_types:
            type_info = type_mappings[quaternion_type]

            yield from _generate_quaternion_class(f"{quaternion_type}Q", f"{type_info.type_name}Q", type_info.type)
            if quaternion_types.index(quaternion_type) < len(quaternion_types) - 1:
                yield f"\n\n"
