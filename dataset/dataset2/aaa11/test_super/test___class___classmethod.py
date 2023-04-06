import unittest
import test_super

def test___class___classmethod():

    class X:

        @classmethod
        def f(cls):
            return __class__
    TestSuper.assertIs(X.f(), X)

TestSuper = test_super.TestSuper()
test___class___classmethod()
