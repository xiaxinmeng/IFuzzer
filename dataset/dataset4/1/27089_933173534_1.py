
def cleanup2():
    try:
        raise OSError
    except OSError as exc:
        saved_exc = exc
    raise MyLibError from saved_exc
