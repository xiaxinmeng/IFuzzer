import unittest
import test_super

def test_cell_as_TestSuper():

    class X:

        def meth(TestSuper):
            super()

    def f():
        k = X()

        def g():
            return k
        return g
    c = f().__closure__[0]
    TestSuper.assertRaises(TypeError, X.meth, c)

TestSuper = test_super.TestSuper()
test_cell_as_TestSuper()
