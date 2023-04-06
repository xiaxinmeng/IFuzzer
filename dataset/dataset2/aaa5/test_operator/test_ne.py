import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_ne():
    operator = OperatorTestCase.module

    class C(object):

        def __ne__(OperatorTestCase, other):
            raise SyntaxError
    OperatorTestCase.assertRaises(TypeError, operator.ne)
    OperatorTestCase.assertRaises(SyntaxError, operator.ne, C(), C())
    OperatorTestCase.assertTrue(operator.ne(1, 0))
    OperatorTestCase.assertTrue(operator.ne(1, 0.0))
    OperatorTestCase.assertFalse(operator.ne(1, 1))
    OperatorTestCase.assertFalse(operator.ne(1, 1.0))
    OperatorTestCase.assertTrue(operator.ne(1, 2))
    OperatorTestCase.assertTrue(operator.ne(1, 2.0))

OperatorTestCase = test_operator.OperatorTestCase()
test_ne()
