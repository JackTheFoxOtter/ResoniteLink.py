from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from resonitelink.models.messages import ImportMeshRawData

from resonitelink.models.assets.mesh.raw_data import BlendshapeFrameRawData
from resonitelink.json import MISSING, json_model, json_element, json_list
from typing import List


__all__ = (
    'BlendshapeRawData',
)


@json_model()
class BlendshapeRawData():
    # Name of the blendshape.
    name : str = json_element("name", str, default=MISSING)

    # Indicates if this blenshape has normal datas.
    has_normal_deltas : bool = json_element("hasNormalDeltas", bool, default=False)

    # Indicates if this blendshape has tangent deltas.
    has_tangent_deltas : bool = json_element("hasTangentDeltas", bool, default=False)

    # Frames that compose this blendshape.
    # Blendshapes need at least 1 frame.
    frames : List[BlendshapeFrameRawData] = json_list("frames", BlendshapeFrameRawData, default=MISSING)

    def _get_binary_data(self, import_msg : 'ImportMeshRawData') -> bytes:
        if not self.frames:
            raise ValueError("Blendshape frames were never provided!")

        data = bytearray()
        for frame in self.frames:
            data.extend(frame._get_binary_data(import_msg, self))
        
        return data
