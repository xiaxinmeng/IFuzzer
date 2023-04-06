class Failure(object):
    def __getattr__(self, attr):
        return (self, None)
issubclass(Failure(), int)
