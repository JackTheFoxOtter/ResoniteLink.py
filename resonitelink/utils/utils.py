def make_first_char_uppercase(value : str) -> str:
    """
    Formats the string so that the first character is uppercase.

    Paramters
    ---------
    value : str
        The string to format.

    Returns
    -------
    The formatted string, the first char will now be uppercase (if it wasn't already).

    """
    if value and len(value) > 0:
        value = value[0].upper() + value[1:]
    
    return value