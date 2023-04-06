
class A:
    def __init__(self, fields=None):
        self.B = dc.make_dataclass('B', fields or [])
        self.B.__module__ = __name__
        # ...
        self.C = self.B()
