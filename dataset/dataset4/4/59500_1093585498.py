class MyMetaHook:
    @classmethod
    def find_module(cls, name, path=None):
        return cls()
    def load_module(self, name):
        raise ImportError("You lose!")