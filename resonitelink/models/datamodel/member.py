from resonitelink.json.models import JSONProperty
from typing import Annotated
from abc import ABC


class Member(ABC):
    member_id : Annotated[str, JSONProperty("id")]