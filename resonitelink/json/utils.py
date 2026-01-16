from .models import JSONModel, JSONPropertyType
from typing import Any, List, Callable

__all__ = (
    'MISSING',
    'is_missing',
    'optional',
    'format_object_structure',
)


class _MissingSentinel:
    """
    Sentinel class used to represent missing values.

    Note
    ----
    Missing values are NOT `null`, they are *missing* (i.e. they won't be included in JSON objects)!

    """
    __slots__ = ()

    def __eq__(self, other) -> bool:
        return False

    def __bool__(self) -> bool:
        return False

    def __hash__(self) -> int:
        return 0

    def __repr__(self):
        return '...'


MISSING: Any = _MissingSentinel()


def is_missing(value : Any) -> bool:
    """
    Checks wether the specified value is "missing" (i.e. is of type `_MissingSentinel`).

    Parameters
    ----------
    value : Any
        The value to check.

    Returns
    -------
    `True` if the provided value has the `_MissingSentinel` type. 

    """
    return type(value) is _MissingSentinel


def optional(value : Any, func : Callable[[], Any]) -> Any:
    """
    If value is MISSING, returns MISSING.
    Otherwise returns result of func.

    """
    if is_missing(value):
        return MISSING
    else:
        return func()


def format_object_structure(obj : Any, print_missing : bool = False, prefix : str = "") -> str:
    """
    Produces a string for the given object that represents that object's structure.
    If that object is an instance of a registered model's data class, it will be resolved recursively.
    This is mainly intended for debugging purposes.

    Parameters
    ----------
    obj : Any
        The object to analyze.
    print_missing : bool
        Wether to list missing property members when resolving model structure.
    prefix : str
        String to prefix before message. Each recursion level pads this with leading spaces.
    
    Returns
    -------
    A string representing the object's structure.

    """
    structure_str : str
    try:
        # Attempt to 
        model = JSONModel.get_for_data_class(type(obj))
    
    except KeyError:
        # Not a model
        structure_str = f"Type '{type(obj).__name__}': {obj}"
    
    else:
        # Model class, resolve children
        property_lines : List[str] = []
        for key, json_property in model.properties.items():
            if hasattr(obj, key):
                # Value for key present
                val = getattr(obj, key)

                if json_property.property_type == JSONPropertyType.LIST and isinstance(val, list):
                    # Resolve property as list
                    property_lines.append(f" - {key} (List):\n{prefix}    - {f'\n{prefix}    - '.join([ format_object_structure(v, prefix=f'{prefix}      ') for v in val ])}")

                elif json_property.property_type == JSONPropertyType.DICT and isinstance(val, dict):
                    # Resolve property as dict
                    property_lines.append(f" - {key} (Dict):\n{prefix}    - {f'\n{prefix}    - '.join([ f'{k}: {format_object_structure(v, prefix=f'{prefix}      ')}' for k, v in val.items() ])}")
                
                else:
                    # Resolve property as single element
                    property_lines.append(f" - {key}: {format_object_structure(val, prefix=f"{prefix}   ")}")
            
            elif print_missing:
                # Value for key missing & missing values should be printed
                property_lines.append(f"{key}: MISSING")
        
        structure_str = f"Type '{type(obj).__name__}' (Data class for model '{model.type_name}'):\n{prefix}{f'\n{prefix}'.join(property_lines)}"

    return structure_str
