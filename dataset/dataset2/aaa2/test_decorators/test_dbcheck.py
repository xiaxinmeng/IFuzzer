import unittest
import test_decorators

def test_dbcheck():

    @test_decorators.dbcheck('args[1] is not None')
    def f(a, b):
        return a + b
    TestDecorators.assertEqual(f(1, 2), 3)
    TestDecorators.assertRaises(test_decorators.DbcheckError, f, 1, None)

TestDecorators = test_decorators.TestDecorators()
test_dbcheck()
