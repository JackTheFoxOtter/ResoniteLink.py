from typing import TypeVar, Any
from abc import ABC
import numpy as np
import quaternionic

from resonitelink.math.array_wrapper import NumpyArrayWrapper


__all__ = (
    'MatrixBase',
    'QuaternionBase',
    'VectorBase',
)


M = TypeVar('M', bound='MatrixBase')
class MatrixBase[T : np.generic](NumpyArrayWrapper[T], ABC):
    def __add__(self : M, other : Any) -> M:
        return self._from_array(np.array(self) + np.array(other))

    def __sub__(self : M, other : Any) -> M:
        return self._from_array(np.array(self) - np.array(other))

    def __mul__(self : M, other : Any) -> M:
        return self._from_array(np.array(self) * np.array(other))
    
    def __div__(self : M, other : Any) -> M:
        return self._from_array(np.array(self) / np.array(other))


Q = TypeVar('Q', bound='QuaternionBase')
class QuaternionBase[T : np.generic](NumpyArrayWrapper[T], ABC):
    def __add__(self : Q, other : Any) -> Q:
        return self._from_array(quaternionic.array(self) + quaternionic.array(other))

    def __sub__(self : Q, other : Any) -> Q:
        return self._from_array(quaternionic.array(self) - quaternionic.array(other))
    
    def __mul__(self : Q, other : Any) -> Q:
        return self._from_array(quaternionic.array(self) * quaternionic.array(other))
    
    def __div__(self : Q, other : Any) -> Q:
        return self._from_array(quaternionic.array(self) / quaternionic.array(other))


V = TypeVar('V', bound='VectorBase')
class VectorBase[T : np.generic](NumpyArrayWrapper[T], ABC):
    """
    Abstract base class of all numeric vectors.
    Defines common mathematical vector operations.
    
    """
    def __add__(self : V, other : Any) -> V:
        return self._from_array(np.array(self) + np.array(other))

    def __sub__(self : V, other : Any) -> V:
        return self.from_array(np.array(self) - np.array(other))

    def __mul__(self : V, other : Any) -> V:
        return self.from_array(np.array(self) * np.array(other))
    
    def __div__(self : V, other : Any) -> V:
        return self.from_array(np.array(self) / np.array(other))

    def cross(self : V, other : V) -> V:
        return self.from_array(np.cross(self, other))

    def dot(self : V, other : V) -> V:
        return self.from_array(np.dot(self, other))

    def magnitude(self : V) -> float: # type: ignore
        return np.linalg.norm(self) # type: ignore

    def normalized(self : V) -> V:
        magnitude = np.linalg.norm(self)
        if magnitude == 0:
            return self
        return self.from_array(self / magnitude) # type: ignore

    @classmethod
    def avg(cls, *vectors : V) -> V:
        return cls.from_array(np.average(vectors, axis=0))
