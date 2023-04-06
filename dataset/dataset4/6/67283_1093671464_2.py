if data[-1] != b'\n'[0]:
    raise UnpicklingError(
        "pickle exhausted before end of frame")