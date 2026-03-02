from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from resonitelink.models.messages.assets.meshes import ImportMeshRawData

from dataclasses import field
from typing import Optional, List
from array import array
from abc import ABC, abstractmethod

from resonitelink.json import abstract_json_model


__all__ = (
    'SubmeshRawData',
)


@abstract_json_model()
class SubmeshRawData(ABC):
    # NOTE: Initializers for indices are in the extending classes!
    _indices : Optional[bytes] = field(default=None, init=False) # int[]

    @property
    def indices(self) -> List[int]:
        if not self._indices:
            raise ValueError("Indices were never provided!")

        arr = array("i")
        arr.frombytes(self._indices)
        return arr.tolist()
    
    @indices.setter
    def indices(self, indices : List[int]):
        self._indices = array("i", indices).tobytes()
    
    def _get_binary_data(self, import_msg : 'ImportMeshRawData') -> bytes:
        if not self._indices:
            raise ValueError("Binary data was never provided!")
        
        return self._indices

    @property
    @abstractmethod
    def index_count(self) -> int:
        raise NotImplementedError()
