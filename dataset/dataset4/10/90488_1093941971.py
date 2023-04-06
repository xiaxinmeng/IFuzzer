class CM:
    def __enter__(self):
        return self
    def __exit__(self, exc: BaseException | None, /):
        if exc is not None:
           print("an exception occurred")