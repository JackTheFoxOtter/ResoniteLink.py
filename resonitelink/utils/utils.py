from resonitelink.models.datamodel import Slot, Reference, Field
from resonitelink.json.models import JSONModel
from resonitelink.json.utils import optional
from resonitelink.proxies import SlotProxy
from typing import Union, Type, Any


def make_first_char_uppercase(value : str) -> str:
    """
    Formats the string so that the first character is uppercase.

    Paramters
    ---------
    value : str
        The string to format.

    Returns
    -------
    The formatted string, the first char will now be uppercase (if it wasn't already).

    """
    if value and len(value) > 0:
        value = value[0].upper() + value[1:]
    
    return value


def get_slot_id(slot : Union[str, Slot, SlotProxy, Reference]) -> str:
    """
    Returns the ID for anything Slot-like.

    """
    if isinstance(slot, str):
        return slot
    
    if isinstance(slot, Slot):
        return slot.id
    
    if isinstance(slot, SlotProxy):
        return slot.id
    
    if isinstance(slot, Reference):
        return slot.id
    
    raise TypeError(f"Unsupported type: {type(slot)}")


def optional_slot_reference(slot : Union[str, Slot, SlotProxy, Reference]):
    """
    If slot is MISSING, returns MISSING.
    Otherwise returns a slot reference for the specified slot.

    """
    return optional(slot, lambda: Reference(get_slot_id(slot), target_type="[FrooxEngine]FrooxEngine.Slot"))


def optional_field(value : Any, field_type : Type[Field]) -> Any:
    """
    If value is MISSING, returns MISSING.
    Otherwise returns a field in the specified type populated with the value.

    """
    return optional(value, lambda: field_type(value=value))

