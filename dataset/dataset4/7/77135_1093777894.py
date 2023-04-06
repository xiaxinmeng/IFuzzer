class FL:
    def __init__(self, func):
        self.func = func
    def __str__(self):
        return self.func()

extra = FL(lambda: f'{extra},waiters:{len(self._waiters)}')