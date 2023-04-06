class BadError(Exception):
    def __init__(self):
        self.i = 0

    def __hash__(self):
        self.i += 1
        return self.i


e = BadError()
raise e from e
