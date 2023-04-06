def load_from_spec(spec):
    _spec = importlib._bootstrap._SpecMethods(spec)
    return _spec.load()