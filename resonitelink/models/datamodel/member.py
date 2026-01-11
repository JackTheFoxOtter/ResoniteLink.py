from resonitelink.json import MISSING, JSONProperty
from dataclasses import dataclass
from typing import Annotated
from abc import ABC


@dataclass
class Member(ABC):
    member_id : Annotated[str, JSONProperty("id")] = MISSING