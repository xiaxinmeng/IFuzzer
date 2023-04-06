while True:
    class D:
        __slots__ = ()
        registry = []
        def __init__(self):
            self.registry.append(self)
    for i in range(100):
        D() and None  # Suppress REPL output.
    del D