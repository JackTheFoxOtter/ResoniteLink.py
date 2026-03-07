from resonitelink.models.datamodel import Float3, Float4, Color
from typing import Any, Iterator, Generator


__all__ = (
    'pack_vectors_float3',
    'unpack_vectors_float3',
    'pack_vectors_float4',
    'unpack_vectors_float4',
    'pack_vectors_color',
    'unpack_vectors_color',
)


def pack_vectors_float3(elements : Iterator[float]) -> Generator[Float3, Any, Any]:
    """
    Yields Float3s from an iterator of floats.

    """
    try:
        while True:
            yield Float3(next(elements), next(elements), next(elements))
    
    except StopIteration:
        pass

def unpack_vectors_float3(vectors : Iterator[Float3]) -> Generator[float, Any, Any]:
    """
    Yields floats for iterator of Float3s.
    
    """
    try:
        while True:
            vector = next(vectors)
            yield vector.x
            yield vector.y
            yield vector.z

    except StopIteration:
        pass

def pack_vectors_float4(elements : Iterator[float]) -> Generator[Float4, Any, Any]:
    """
    Yields Float3s from an iterator of floats.

    """
    try:
        while True:
            yield Float4(next(elements), next(elements), next(elements))
    
    except StopIteration:
        pass

def unpack_vectors_float4(vectors : Iterator[Float4]) -> Generator[float, Any, Any]:
    """
    Yields floats for iterator of Float3s.
    
    """
    try:
        while True:
            vector = next(vectors)
            yield vector.x
            yield vector.y
            yield vector.z
            yield vector.w

    except StopIteration:
        pass

def pack_vectors_color(elements : Iterator[float]) -> Generator[Color, Any, Any]:
    """
    Yields Colors from an iterator of floats.

    """
    try:
        while True:
            yield Color(next(elements), next(elements), next(elements), next(elements))
    
    except StopIteration:
        pass

def unpack_vectors_color(colors : Iterator[Color]) -> Generator[float, Any, Any]:
    """
    Yields floats for iterator of Colors.
    
    """
    try:
        while True:
            color = next(colors)
            yield color.r
            yield color.g
            yield color.b
            yield color.a

    except StopIteration:
        pass