
@functools.decorator_factory
def dataclass(cls, /, *, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False):
    return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
