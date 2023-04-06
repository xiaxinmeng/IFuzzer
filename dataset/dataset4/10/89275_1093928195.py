class ExcA(Exception):
    def __init__(self, want):
        msg = "missing "
        msg += want
        super().__init__(msg)
    def __reduce__(self):
        return (type(self), self.args, self.args)
    def __setstate__(self, state):
        self.args = stat