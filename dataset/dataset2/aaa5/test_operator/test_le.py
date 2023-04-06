import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_le():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.le)
    OperatorTestCase.assertRaises(TypeError, operator.le, 1j, 2j)
    OperatorTestCase.assertFalse(operator.le(1, 0))
    OperatorTestCase.assertFalse(operator.le(1, 0.0))
    OperatorTestCase.assertTrue(operator.le(1, 1))
    OperatorTestCase.assertTrue(operator.le(1, 1.0))
    OperatorTestCase.assertTrue(operator.le(1, 2))
    OperatorTestCase.assertTrue(operator.le(1, 2.0))

OperatorTestCase = test_operator.OperatorTestCase()
test_le()
