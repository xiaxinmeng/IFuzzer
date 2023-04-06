import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_gt():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.gt)
    OperatorTestCase.assertRaises(TypeError, operator.gt, 1j, 2j)
    OperatorTestCase.assertTrue(operator.gt(1, 0))
    OperatorTestCase.assertTrue(operator.gt(1, 0.0))
    OperatorTestCase.assertFalse(operator.gt(1, 1))
    OperatorTestCase.assertFalse(operator.gt(1, 1.0))
    OperatorTestCase.assertFalse(operator.gt(1, 2))
    OperatorTestCase.assertFalse(operator.gt(1, 2.0))

OperatorTestCase = test_operator.OperatorTestCase()
test_gt()
