from decimal import Decimal
from typing import TypeAlias
import numpy as np


__all__ = (
    't_bool',
    't_byte',
    't_sbyte',
    't_ushort',
    't_short',
    't_uint',
    't_int',
    't_ulong',
    't_long',
    't_float',
    't_double',
    't_decimal',
    't_char',
    't_string',
    't_uri',
    't_datetime',
    't_timespan',
)


# Type aliases for standalone types
t_bool : TypeAlias = np.bool
t_byte : TypeAlias = np.ubyte
t_sbyte : TypeAlias = np.byte
t_ushort : TypeAlias = np.uint16
t_short : TypeAlias = np.int16
t_uint : TypeAlias = np.uint32
t_int : TypeAlias = np.int32
t_ulong : TypeAlias = np.uint64
t_long : TypeAlias = np.int64
t_float : TypeAlias = np.float32
t_double : TypeAlias = np.float64
t_decimal : TypeAlias = Decimal
t_char : TypeAlias = str
t_string : TypeAlias = str
t_uri : TypeAlias = str
t_datetime : TypeAlias = str
t_timespan : TypeAlias = str
