import unittest
import test_super

def test___class___instancemethod():

    class X:

        def f(TestSuper):
            return __class__
    TestSuper.assertIs(X().f(), X)

TestSuper = test_super.TestSuper()
test___class___instancemethod()
