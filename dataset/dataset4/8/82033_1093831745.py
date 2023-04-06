import pickle

class Spam:
    def __eggs(self):
        pass
    def eggs(self):
        return pickle.dumps(self.__eggs)

spam = Spam()
pkl = spam.eggs()                       # Succeeds via implicit mangling (but pickles unmangled name)
pickle.loads(pkl)                       # Fails (tried to load __eggs