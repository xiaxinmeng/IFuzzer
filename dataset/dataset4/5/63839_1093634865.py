class classattr:
    def __init__(self, getter):
        self.getter = getter
    def __get__(self, obj, cls):
        return self.getter(cls)