import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_contains():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.contains)
    OperatorTestCase.assertRaises(TypeError, operator.contains, None, None)
    OperatorTestCase.assertRaises(ZeroDivisionError, operator.contains, BadIterable(), 1)
    OperatorTestCase.assertTrue(operator.contains(range(4), 2))
    OperatorTestCase.assertFalse(operator.contains(range(4), 5))

OperatorTestCase = test_operator.OperatorTestCase()
test_contains()
