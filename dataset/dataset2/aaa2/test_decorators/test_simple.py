import unittest
import test_decorators

def test_simple():

    def plain(x):
        x.extra = 'Hello'
        return x

    @plain
    class C(object):
        pass
    TestClassDecorators.assertEqual(C.extra, 'Hello')

TestClassDecorators = test_decorators.TestClassDecorators()
test_simple()
