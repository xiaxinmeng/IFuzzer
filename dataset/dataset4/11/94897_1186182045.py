T = typing.TypeVar("T")

class GenericDependency(typing.Generic[T]):
    pass

class DependingConcrete:
    def __init__(self, dep: GenericDependency):
        # the type hint for `dep` is the concrete class GenericDependency
        pass


class DependingGeneric(typing.Generic[T]):
    def __init__(self, dep: GenericDependency[T]):
        # to find the concrete class of `dep` we need to look at the type hint's `__origin__`, which is kind of cumbersome, 
        # and may easily conflict with other logic that deals with `__origin__` on other classes like the `_GenericAlias` ones,
        # but not insurmountable
        pass