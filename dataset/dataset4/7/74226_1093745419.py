class A:
    def __init__(self, **kwargs):
        self._extra = kwargs

xa = [A() for _ in range(1000)]