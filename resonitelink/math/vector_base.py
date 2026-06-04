from resonitelink.math.array_wrapper import NumpyArrayWrapper
from typing import TypeVar, Any
from abc import ABC
import numpy as np


__all__ = (
    'VectorBase',
)


V = TypeVar('V', bound='VectorBase')
class VectorBase[T : np.generic](NumpyArrayWrapper[T], ABC):
    """
    Abstract base class of all numeric vectors.
    Defines common mathematical vector operations.
    
    """
    def __add__(self : V, other : Any) -> V:
        return self._from_array(np.array(self) + np.array(other)) # type: ignore

    def __sub__(self : V, other : Any) -> V:
        return self.from_array(np.array(self) - np.array(other)) # type: ignore

    def __mul__(self : V, other : Any) -> V:
        return self.from_array(np.array(self) * np.array(other)) # type: ignore
    
    def __div__(self : V, other : Any) -> V:
        return self.from_array(np.array(self) / np.array(other)) # type: ignore

    def cross(self : V, other : V) -> V:
        return self.from_array(np.cross(self, other)) # type: ignore

    def dot(self : V, other : V) -> V:
        return self.from_array(np.dot(self, other)) # type: ignore

    def magnitude(self : V) -> float:
        return np.linalg.norm(self) # type: ignore

    def normalized(self : V) -> V:
        magnitude = np.linalg.norm(self)
        if magnitude == 0:
            return self # type: ignore
        return self.from_array(self / magnitude) # type: ignore

    @classmethod
    def avg(cls, *vectors : V) -> V:
        return cls.from_array(np.average(vectors, axis=0)) # type: ignore
