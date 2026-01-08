from resonitelink.json import JSONProperty
from typing import Annotated

class MessageBase():
    message_id : Annotated[str, JSONProperty("messageId")]
