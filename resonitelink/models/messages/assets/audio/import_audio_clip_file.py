from resonitelink.models.messages import Message
from resonitelink.json import JSONProperty, json_model
from dataclasses import dataclass


@json_model("importAudioClipFile")
@dataclass(slots=True)
class ImportAudioClipFile(Message):
    pass