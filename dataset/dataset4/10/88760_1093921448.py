exc = foo()
try:
    raise exc
finally:
    exc.__context__ = None