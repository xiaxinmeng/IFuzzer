def g():
    yield iter(None)
list(*g())