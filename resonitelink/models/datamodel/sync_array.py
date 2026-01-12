from resonitelink.models.datamodel import Member
from resonitelink.json import JSONProperty
from dataclasses import dataclass
from typing import Annotated, List, Any
from abc import ABC, abstractmethod


@dataclass(slots=True)
class SyncArray(Member, ABC):
    values : Annotated[List[Any], JSONProperty("values", abstract=True)]

    @property
    @abstractmethod
    def element_type(self) -> str:
        raise NotImplementedError()
