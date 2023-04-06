def filtered_exc(exc_type, *, unless=()):
    class _FilteredException(metaclass=FilteredExceptionMeta):
        @classmethod
        def __subclasshook__(cls, other):
            return (issubclass(other, exc_type)
                    and not issubclass(other, unless))
    return _FilteredException