from resonitelink.json import MISSING, JSONProperty
from dataclasses import dataclass
from typing import Annotated
from abc import ABC


@dataclass
class Worker(ABC):
    worker_id : Annotated[str, JSONProperty("id")] = MISSING
    is_reference_only : Annotated[bool, JSONProperty("isReferenceOnly")] = MISSING
