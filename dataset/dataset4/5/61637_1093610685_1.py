def __init__(self, interval, function, args=None, kwargs=None):
    ...
    self.args = args if args is not None else []
    self.kwargs = kwargs if kwargs is not None else {}