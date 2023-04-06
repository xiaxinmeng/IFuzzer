if data[-1] != b'\n':
    raise UnpicklingError(
        "pickle exhausted before end of frame")