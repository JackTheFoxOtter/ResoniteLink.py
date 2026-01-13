from typing import TypeVar, Generic, Dict
from random import randint


ValueT = TypeVar("ValueT")
class IDRegistry(Generic[ValueT]):
    """
    Helper class for generating and keeping track of IDs.
    
    """
    _next_registry_id : int = 0x00
    _global_prefix : str = f"RLPY_{randint(0x0000, 0xFFFF):0{4}X}_" # TODO: We'll probably get a unique client ID from ResoniteLink in the future, then we can replace this random value with it.
    
    _registry_id : int
    _prefix : str
    _next_id_num : int
    _ids : Dict[str, ValueT]

    def __init__(self):
        """
        Creates a new ID registry instance.

        """
        self._registry_id = IDRegistry._next_registry_id
        self._prefix = f"{IDRegistry._global_prefix}{self._registry_id:0{2}X}_"
        self._next_id_num = 0
        self._ids = {}

        IDRegistry._next_registry_id += 1 # Increment global next registry ID
    
    def generate_id(self, value : ValueT = None) -> str:
        """
        Generates a new ID and returns it.

        id_meta : Any
            Optional meta-value associated with this ID. Can be anything!

        """
        id = f"{self._prefix}{self._next_id_num:X}"
        self._ids[id] = value

        self._next_id_num += 1 # Increment next ID value

        return id
    
    def get_id_value(self, id : str) -> ValueT:
        """
        Retrieves the value associated with an ID.
        If the value is only needed once, consider using pop_id_value.

        Parameters
        ----------
        id : str
            The ID to retrieve the associated value of.

        Returns
        -------
        The value associated with this ID.

        Raises
        ------
        KeyError if the ID is unknown, or the ID value was already consumed (by using `pop_id_value`).

        """
        return self._ids[id]

    def pop_id_value(self, id : str) -> ValueT:
        """
        Retrieves the value associated with an id and removes it from the registry.
        This can only be called once per ID!

        Parameters
        ----------
        id : str
            The ID to retrieve the associated value of.

        Returns
        -------
        The value associated with this ID.

        Raises
        ------
        KeyError if the ID is unknown, or the ID value was already consumed (by using `pop_id_value`).

        """
        return self._ids.pop(id)
