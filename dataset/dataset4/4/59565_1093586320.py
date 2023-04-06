class SillyDict(dict):
    def __getitem__(self, key):
        return "hello"

obj.__dict__ = SillyDict()