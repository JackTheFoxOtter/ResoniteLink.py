from resonitelink.math.array_wrapper import NumpyArrayWrapper
from abc import ABC
import numpy as np


__all__ = (
    'VectorBase',
)


class VectorBase[T : np.generic](NumpyArrayWrapper[T], ABC):
    """
    Abstract base class of all numeric vectors.
    Defines common mathematical vector operations.
    
    """
    def cross(self, other : 'VectorBase'):
        return self.from_array(np.cross(self, other)) # type: ignore
