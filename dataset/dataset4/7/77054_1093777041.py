class _GenericAlias:
    ...
    def __reduce__(self):
        if self._special:
            return 'typing.' + self._name
        return super().__reduce__()