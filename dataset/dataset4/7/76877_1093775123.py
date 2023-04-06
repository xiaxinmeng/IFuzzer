import pickle
class MultipleArgumentsError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

pickle.loads(pickle.dumps(MultipleArgumentsError('a', 'b')))