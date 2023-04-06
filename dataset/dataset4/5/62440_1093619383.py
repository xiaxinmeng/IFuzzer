if not isinstance(msg, bytes):
    raise TypeError("expected bytes, but got %r" % type(msg).__name__)