
__import__('json').dumps(object(), default=lambda o: repr(o).encode())
