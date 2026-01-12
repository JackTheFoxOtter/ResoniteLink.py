from resonitelink.json import MISSING, JSONProperty
from dataclasses import dataclass
from typing import Annotated
from abc import ABC


@dataclass(slots=True)
class Member(ABC):
    id : Annotated[str, JSONProperty("id")] = MISSING
