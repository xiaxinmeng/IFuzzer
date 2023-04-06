class mydict(dictionary):
    def __setitem__(self, key, value):
        pass

d = mydict()
del d['b'] # This line raises SystemError.
--- end