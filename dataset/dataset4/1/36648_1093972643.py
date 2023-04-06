def __call__(self):
    return lambda: 1

__call__ = property(__call__)