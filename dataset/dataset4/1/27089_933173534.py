def cleanup():
    try:
        raise OSError   # the original exception
    except OSError as exc:
        raise MyLibError from exc   # a wrapper exception, whose __cause__ points to the original exception