from datetime import datetime, timezone
from typing import Union

from resonitelink.json import MISSING, json_model, json_element


__all__ = (
    'ResoniteLinkSession',
)


@json_model()
class ResoniteLinkSession():
    session_name : str = json_element("sessionName", str, default=MISSING)
    session_id : str = json_element("sessionID", str, default=MISSING)
    link_port : int = json_element("linkPort", int, default=MISSING)

    last_updated : Union[datetime, None] = None

    def is_expired(self, expiration_seconds : float) -> bool:
        """
        Checks wether this session is expired by comparing its expiration time to the current time.

        Raises
        ------
        ValueError
            When the last_updated parameter has not been set yet.

        """
        if (not self.last_updated):
            raise ValueError("The session was not yet updated!")

        return (datetime.now(tz=timezone.utc) - self.last_updated).total_seconds() > expiration_seconds
