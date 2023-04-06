import unittest
import test_decorators

def test_order():

    def applied_first(x):
        x.extra = 'first'
        return x

    def applied_second(x):
        x.extra = 'second'
        return x

    @applied_second
    @applied_first
    class C(object):
        pass
    TestDecorators.assertEqual(C.extra, 'second')

TestDecorators = test_decorators.TestDecorators()
test_order()
