import unittest
import test_decorators

def test_single():

    class C(object):

        @staticmethod
        def foo():
            return 42
    TestDecorators.assertEqual(C.foo(), 42)
    TestDecorators.assertEqual(C().foo(), 42)

TestDecorators = test_decorators.TestDecorators()
test_single()
