import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_ge():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.ge)
    OperatorTestCase.assertRaises(TypeError, operator.ge, 1j, 2j)
    OperatorTestCase.assertTrue(operator.ge(1, 0))
    OperatorTestCase.assertTrue(operator.ge(1, 0.0))
    OperatorTestCase.assertTrue(operator.ge(1, 1))
    OperatorTestCase.assertTrue(operator.ge(1, 1.0))
    OperatorTestCase.assertFalse(operator.ge(1, 2))
    OperatorTestCase.assertFalse(operator.ge(1, 2.0))

OperatorTestCase = test_operator.OperatorTestCase()
test_ge()
