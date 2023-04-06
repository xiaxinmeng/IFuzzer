class Namespace(types.SimpleNamespace):
    """..."""
    def __contains__(self, key):
        return key in self.__dict__