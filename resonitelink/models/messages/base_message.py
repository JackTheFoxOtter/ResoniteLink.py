from resonitelink.json import MISSING, JSONProperty
from dataclasses import dataclass
from typing import Annotated
from abc import ABC


@dataclass
class BaseMessage(ABC):
    message_id : Annotated[str, JSONProperty("messageId")] = MISSING
