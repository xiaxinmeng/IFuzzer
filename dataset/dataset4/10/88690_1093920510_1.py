def __getattr__(self, attr):
    # We are careful for copy and pickle.
    # Also for simplicity we just don't relay all dunder names
    if '__origin__' in self.__dict__ and not _is_dunder(attr):
        return getattr(self.__origin__, attr)
    raise AttributeError(attr)