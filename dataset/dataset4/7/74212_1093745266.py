from collections.abc import Hashable
class X: pass
assert issubclass(X, Hashable)
x = X()

class X(Hashable): pass
assert issubclass(X, Hashable)
x = X() # Can't instantiate abstract class X with abstract methods