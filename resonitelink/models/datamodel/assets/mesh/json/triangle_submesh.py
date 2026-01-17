from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated, List

from .triangle import Triangle
from .submesh import Submesh


@json_model("triangleSubmesh") # TODO: Anonymous model
@dataclass(slots=True)
class TriangleSubmesh(Submesh):
    """
    A submesh composed of individual triangles.
    
    """
    # All the triangles that form this submesh.
    triangles : Annotated[List[Triangle], JSONProperty("triangles")] = MISSING


@json_model("triangleSubmeshFlat") # TODO: Anonymous model
@dataclass(slots=True)
class TriangleSubmeshFlat(Submesh):
    """
    A submesh composed of individual triangles.
    This is an alternate representation and will result in same submesh as TriangleSubmesh
    With this representation you must take care to provide the indicies for each triangle properly.
    Each triangle requires three indicies. Those indicies are consecutive.
    
    """
    # Indexes of vertices representing triangles of this mesh.
    # Note that each triangle needs three consecutive indicies in this list.
    vertex_indices : Annotated[List[int], JSONProperty("vertexIndices")] = MISSING
