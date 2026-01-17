from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated
from abc import ABC, abstractmethod


@dataclass(slots=True)
class SubmeshRawData(ABC):
    @property
    @abstractmethod
    def indices_count(self) -> int:
        raise NotImplementedError()
