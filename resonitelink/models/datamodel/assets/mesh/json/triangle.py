from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("triangle") # TODO: Anonymous
@dataclass(slots=True)
class Triangle():
    """
    Represents a single triangle of a mesh.
    
    """
    # Index of the first vertex that forms this triangle.
    vertex_0_index : Annotated[int, JSONProperty("vertex0Index")] = MISSING

    # Index of the second vertex that forms this triangle.
    vertex_1_index : Annotated[int, JSONProperty("vertex0Index")] = MISSING

    # Index of the third vertex that forms this triangle.
    vertex_2_index : Annotated[int, JSONProperty("vertex0Index")] = MISSING
