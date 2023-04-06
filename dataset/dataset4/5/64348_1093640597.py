import threading

class Foo(object):
#       Uncommenting these yields "NoneType is not callable" rather than an AttributeError
#       __enter__ = None
#       __exit__ = None
#       acquire = None
#       release = None
#       lock = None

        def __init__(self):
                self.lock = threading.RLock()
                print(repr(self.lock))
                self.__enter__ = self.lock.__enter__
                self.__exit__ = self.lock.__exit__
                self.acquire = self.lock.acquire
                self.release = self.lock.release

foo = Foo()
# These all function as expected.  The fourth line fails (correctly) on 2.7.5.
print(repr(foo.__enter__))
print(repr(foo.__exit__))
print(foo.__enter__())
print(foo.__exit__())

# This does not
with foo:
        pass