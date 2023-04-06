import unittest
import test_super

def test_obscure_super_errors():

    def f():
        super()
    TestSuper.assertRaises(RuntimeError, f)

    def f(x):
        del x
        super()
    TestSuper.assertRaises(RuntimeError, f, None)

    class X:

        def f(x):
            nonlocal __class__
            del __class__
            super()
    TestSuper.assertRaises(RuntimeError, X().f)

TestSuper = test_super.TestSuper()
test_obscure_super_errors()
