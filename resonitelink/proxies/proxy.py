from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # Only for type hints, prevents circular import
    from resonitelink import ResoniteLinkClient

from resonitelink.models.datamodel import Member, Worker
from typing import TypeVar, Generic, Union, Optional
from abc import ABC, abstractmethod


TData = TypeVar("TData", bound=Union[Member, Worker])
class Proxy(Generic[TData], ABC):
    """
    Proxy objects provide a utility wrapper around data model objects.
    They allow for:
    * A way to represent a model object who's ID is known, but the actual data has not been fetched yet.
    * A way to add additional functionality to model objects without "polluting" the data class with non-data functionality.
    Proxies are always in the context of a client.
    
    """
    _client : ResoniteLinkClient
    _id : str
    _data : Optional[TData]

    @property
    def client(self) -> ResoniteLinkClient:
        return self._client
    
    @property
    def id(self) -> str:
        return self._id

    def __init__(self, client : ResoniteLinkClient, id : str, data : Optional[TData] = None):
        self._client = client
        self._id = id
        self._data = data

    async def get_data(self) -> TData:
        """
        Gets the data object associated with this proxy.
        Fetches the data if it wasn't fetched yet.

        Returns
        -------
        The cached or fetched data object.

        Raises
        ------
        RuntimeError
            When fetching the data didn't return any data.

        """
        if self._data is None:
            # Load the data initially
            data = await self.fetch_data()
            if data is None:
                # Data still None after fetching, this is not allowed to happen
                raise RuntimeError(f"Proxy {self} error: Fetched data is `None`!")
            
            self._data = data
        
        return self._data
    
    def invalidate_data(self):
        """
        Invalidates this proxy's data.

        """
        self._data = None

    @abstractmethod
    async def fetch_data(self) -> TData:
        raise NotImplementedError()
