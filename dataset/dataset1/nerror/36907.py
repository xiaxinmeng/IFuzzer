class IntWithDict:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    def __index__(self):
        self.kwargs.clear()
        L = [2**i for i in range(10000)]
        return 0
x = IntWithDict(dont_inherit=float())
compile("", "", "", x, **x.kwargs)
