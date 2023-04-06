import inspect
class X(object):
    def a(self):pass
    def b(self):pass
    def c(self):pass

print(inspect.getmembers(X, predicate=inspect.ismethod))
print(inspect.getmembers(X, predicate=inspect.isfunction))