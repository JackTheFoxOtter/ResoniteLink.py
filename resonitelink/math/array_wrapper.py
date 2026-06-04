from numpy.typing import NDArray
from typing import List, Tuple, Type, TypeVar
from numpy import generic, array
from abc import ABC, abstractmethod


__all__ = (
    'NumpyArrayWrapper',
)


A = TypeVar('A', bound='NumpyArrayWrapper')
class NumpyArrayWrapper[T : generic](ABC):
    """
    Abstract base class for all types that are wrapped into Numpy arrays (currently vectors & matrices).
    
    """
    @classmethod
    @abstractmethod
    def _get_array_shape(cls) -> Tuple[int, ...]:
        raise NotImplementedError()
    
    @classmethod
    @abstractmethod
    def _get_element_type(cls) -> Type[T]:
        raise NotImplementedError()
    
    @classmethod
    @abstractmethod
    def _from_array(cls, array : NDArray[T]) -> A: # type: ignore
        raise NotImplementedError()

    @classmethod
    def from_array(cls, array : NDArray[T]) -> A: # type: ignore
        if array.shape != cls._get_array_shape():
            raise ValueError(f"Invalid array shape for {cls.__name__}: {array.shape} (Expected: {cls._get_array_shape()})")
        
        return cls._from_array(array)
    
    @abstractmethod
    def get_elements(self) -> List[T]:
        raise NotImplementedError()
    
    def __array__(self, dtype=None, copy=None):
        # NOTE: dtype is ignored! The returned array always uses the type specified by the implementation.
        if copy is False:
            raise ValueError("copy=False isn't supported. A copy is always created.")

        return array(self.get_elements(), dtype=self._get_element_type())
