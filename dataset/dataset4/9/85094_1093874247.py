import pickle
class StrRegexError(Exception):
    def __init__(self, *, pattern):
        self.pattern = pattern

data = pickle.dumps(StrRegexError(pattern='test'))
instance = pickle.loads(data)