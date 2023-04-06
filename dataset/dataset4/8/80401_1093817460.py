class NS(dict):

    def __setitem__(self, k, v):
        if not isinstance(v, type(lambda: 0)):
            raise RuntimeError("Global variables considered harmful")

globals = NS()

exec("foo = 1", globals)