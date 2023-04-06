class MetaWarm(type):
    def __instancecheck__(cls, inst):
        return inst in {'red', 'orange', 'blue'}

class Warm(metaclass=MetaWarm):
    pass