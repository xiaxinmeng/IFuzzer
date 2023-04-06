import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_lt():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.lt)
    OperatorTestCase.assertRaises(TypeError, operator.lt, 1j, 2j)
    OperatorTestCase.assertFalse(operator.lt(1, 0))
    OperatorTestCase.assertFalse(operator.lt(1, 0.0))
    OperatorTestCase.assertFalse(operator.lt(1, 1))
    OperatorTestCase.assertFalse(operator.lt(1, 1.0))
    OperatorTestCase.assertTrue(operator.lt(1, 2))
    OperatorTestCase.assertTrue(operator.lt(1, 2.0))

OperatorTestCase = test_operator.OperatorTestCase()
test_lt()
