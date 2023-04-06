M = TypeVar("M")

class SingletonMeta(type):
    """Metaclass for single value classes."""
    def __call__(cls: Type[M], *args: Any, **kwargs: Any) -> M:

        ### Never see this line of output
        print(f"{cls.__name__}.__call__({args=}, {kwargs=}")