class myCounter(Counter):
    def __init__(self, bar, *args):
        self.foo = bar
        super().__init__(*args)

class myDict(dict):
    def __init__(self, bar, *args):
        self.foo = bar
        super().__init__(*args)

c = myCounter("bar")
l = myDict("bar")
print(c.foo) # prints bar
print(l.foo) # prints bar

cc = copy.copy(c)
ll = copy.copy(l)
print(cc.foo) # prints {}
print(ll.foo) # prints bar