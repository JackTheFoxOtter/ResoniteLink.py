from typing import Any


class _MissingSentinel:
    """
    Sentinel class used to represent missing values.

    Note
    ----
    Missing values are NOT `null`, they are *missing* (i.e. they won't be included in JSON objects)!

    """
    __slots__ = ()

    def __eq__(self, other) -> bool:
        return False

    def __bool__(self) -> bool:
        return False

    def __hash__(self) -> int:
        return 0

    def __repr__(self):
        return '...'


MISSING: Any = _MissingSentinel()


def is_missing(value : Any) -> bool:
    """
    Checks wether the specified value is "missing" (i.e. is of type `_MissingSentinel`).

    Parameters
    ----------
    value : Any
        The value to check.

    Returns
    -------
    `True` if the provided value has the `_MissingSentinel` type. 

    """
    return type(value) is _MissingSentinel