def _validate_float(value):
    """
    Coerce an arbitrary Python object to a float, or raise TypeError.
    """
    if type(value) is float:  # fast path for common case
        return value
    try:
        nb_float = type(value).__float__
    except AttributeError:
        raise TypeError(
            "Object of type {!r} not coerceable to float".format(type(value)))
    return nb_float(value)