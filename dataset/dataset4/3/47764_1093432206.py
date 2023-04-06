########################################
import pickle

class Foo:
    def __getattr__(self, key):
        self.foo

with open('foo.db', 'wb') as f:
    foo = Foo()
    pickle.dump(foo, f)

with open('foo.db', 'rb') as f:
    pickle.load(f)
########################################