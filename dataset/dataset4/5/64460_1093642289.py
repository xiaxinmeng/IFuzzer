class Picky:
    def __getstate__(self):
        return {}
    def __getattr__(self, attr):
        return None