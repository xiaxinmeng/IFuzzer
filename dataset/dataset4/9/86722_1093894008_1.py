
class A:
    def m(self, a=None): pass

from unittest import mock
with mock.patch.object(A, "m"):
    A.m.side_effect = print
    A().m(1)
