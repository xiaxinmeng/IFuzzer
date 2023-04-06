
class A:
    def m(self, a=None): pass

def descriptor(self, obj, objtype=None):
    self._self = obj
    def _(*args):
        return self(obj, *args)
    return _

from unittest import mock
with mock.patch.object(A, "m"):
    A.m.side_effect = print
    A.m.__get__ = descriptor
    A().m(1)
