err = ValueError()
try:
    raise KeyError
except Exception:
    raise err