import pickle

class ExcA(Exception):
    def __init__(self, want):
        msg = "missing "
        msg += want
        super().__init__(msg)

ExcA('bb')   # this will output ExcA("missing bb"), which is good
pickle.loads(pickle.dumps(ExcA('bb')))  # this will output ExcA("missing missing bb"), which is different from `ExcA('bb')`