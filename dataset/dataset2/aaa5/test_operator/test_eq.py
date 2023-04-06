import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_eq():
    operator = OperatorTestCase.module

    class C(object):

        def __eq__(OperatorTestCase, other):
            raise SyntaxError
    OperatorTestCase.assertRaises(TypeError, operator.eq)
    OperatorTestCase.assertRaises(SyntaxError, operator.eq, C(), C())
    OperatorTestCase.assertFalse(operator.eq(1, 0))
    OperatorTestCase.assertFalse(operator.eq(1, 0.0))
    OperatorTestCase.assertTrue(operator.eq(1, 1))
    OperatorTestCase.assertTrue(operator.eq(1, 1.0))
    OperatorTestCase.assertFalse(operator.eq(1, 2))
    OperatorTestCase.assertFalse(operator.eq(1, 2.0))

OperatorTestCase = test_operator.OperatorTestCase()
test_eq()
