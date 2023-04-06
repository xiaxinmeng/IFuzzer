class composable:

    def __init__(self, func):
        self.func = func

    def __call__(self, arg):
        return self.func(arg)

    def __matmul__(self, other):
        def composition(*args, **kwargs):
            return self.func(other(*args, **kwargs))
        return composable(composition)