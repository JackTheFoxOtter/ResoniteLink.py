from resonitelink.models.messages import Message
from resonitelink.json import json_model
from dataclasses import dataclass


@json_model("requestSessionData")
@dataclass(slots=True)
class RequestSessionData(Message):
    pass