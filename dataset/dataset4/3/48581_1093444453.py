class partialmethod(functools.partial):
    def __get__(self, obj, cls):
        if obj is None:
            return self
        return functools.partial(self.func,
                                 *((obj,) + self.args),
                                 **self.keywords)
    def __call__(*args, **kwds):
        self, *args = args
        call_kwds = {}
        call_kwds.update(self.keywords)
        call_kwds.update(kwds)
        return self.func(self,
                         *(self.args + args),
                         **call_kwds)

class C:
    def example(self, *args, **kwds):
        print(self, args, kwds)
    fails = functools.partial(example, 1, 2, 3, x=1)
    works = partialmethod(example, 1, 2, 3, x=1)