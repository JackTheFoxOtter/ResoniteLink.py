from resonitelink.models.responses import Response


class ResoniteLinkException(Exception):
    """
    Base class for all exceptions that result on the ResoniteLink server-side and are received as error messages. 
    
    """
    _error_info : str

    def __init__(self, response : Response):
        """
        Creates a new instance.

        Parameters
        ----------
        message : str
            The error info received in the ResoniteLink error message.

        """
        self._error_info = response.error_info
    
    def __str__(self) -> str:
        return self._error_info
