def _strerror(err):
    try:
        return strerror(err)
    except (ValueError, OverflowError):
        if err in errorcode:
            return errorcode[err]
        return "Unknown error %s" %err