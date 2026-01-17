from resonitelink.models.messages import BinaryPayloadMessage
from resonitelink.json import JSONProperty, json_model
from dataclasses import dataclass


@json_model("importAudioClipRawData")
@dataclass(slots=True)
class ImportAudioClipRawData(BinaryPayloadMessage):
    pass