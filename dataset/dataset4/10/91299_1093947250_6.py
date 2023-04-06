cls = type(self._cls)(...)
for item in cls.__dict__.values():
    ... # update closures
return cls