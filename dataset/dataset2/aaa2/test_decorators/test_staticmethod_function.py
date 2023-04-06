import unittest
import test_decorators

def test_staticmethod_function():

    @staticmethod
    def notamethod(x):
        return x
    TestDecorators.assertRaises(TypeError, notamethod, 1)

TestDecorators = test_decorators.TestDecorators()
test_staticmethod_function()
