from resonitelink.json import MISSING, JSONProperty
from dataclasses import dataclass
from typing import Annotated
from abc import ABC, abstractmethod


@dataclass(slots=True)
class Message(ABC):
    message_id : Annotated[str, JSONProperty("messageId")] = MISSING


@dataclass(slots=True)
class BinaryPayloadMessage(Message, ABC):
    @property
    @abstractmethod
    def raw_binary_payload(self) -> bytes:
        raise NotImplementedError()

    @raw_binary_payload.setter
    @abstractmethod
    def raw_binary_payload(self, data : bytes):
        raise NotImplementedError()
