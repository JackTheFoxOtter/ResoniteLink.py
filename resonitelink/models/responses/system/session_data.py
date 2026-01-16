from resonitelink.models.responses import Response
from resonitelink.json import MISSING, JSONProperty, json_model
from dataclasses import dataclass
from typing import Annotated


@json_model("sessionData")
@dataclass(slots=True)
class SessionData(Response):
    resonite_version : Annotated[str, JSONProperty("resoniteVersion")] = MISSING
    resonite_link_version : Annotated[str, JSONProperty("resoniteLinkVersion")] = MISSING
    unique_session_id : Annotated[str, JSONProperty("UniqueSessionId")] = MISSING
