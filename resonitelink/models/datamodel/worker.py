from resonitelink.json.models import JSONProperty
from typing import Annotated
from abc import ABC


class Worker(ABC):
    worker_id : Annotated[str, JSONProperty("id")]
    is_reference_only : Annotated[bool, JSONProperty("isReferenceOnly")]
