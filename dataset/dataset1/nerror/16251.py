from copy import deepcopy

class Spam(dict):
    def __getattr__(self, name):
        # defaults to None
        return self.get(name)

deepcopy(Spam(ham=5))
