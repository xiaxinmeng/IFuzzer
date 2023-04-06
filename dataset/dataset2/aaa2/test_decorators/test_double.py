import unittest
import test_decorators

def test_double():

    def ten(x):
        x.extra = 10
        return x

    def add_five(x):
        x.extra += 5
        return x

    @add_five
    @ten
    class C(object):
        pass
    TestDecorators.assertEqual(C.extra, 15)

TestDecorators = test_decorators.TestDecorators()
test_double()
