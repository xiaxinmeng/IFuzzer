class Descriptor(Generic[T]):
    def __init__(self, *, default: T):
        self._default = default

    def __get__(self, __obj: object | None, __owner: Any) -> T:
        if __obj is None:
            return self._default