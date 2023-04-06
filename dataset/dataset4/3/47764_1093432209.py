########################
import pickle

class Foo:
    def __getattr__(self, key):
        self.foo

f = open('foo.db', 'w')
foo = Foo()
pickle.dump(foo, f)
f.close()

f = open('foo.db', 'r')
pickle.load(f)
f.close()
########################