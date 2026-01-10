from resonitelink.json import JSONProperty
from typing import Annotated
from abc import ABC

class BaseMessage(ABC):
    message_id : Annotated[str, JSONProperty("messageId")]
