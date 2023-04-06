class D(dict):
    def __missing__(self, key):
        return None
d = D()