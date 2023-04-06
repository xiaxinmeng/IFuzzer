import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_abs():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.abs)
    OperatorTestCase.assertRaises(TypeError, operator.abs, None)
    OperatorTestCase.assertEqual(operator.abs(-1), 1)
    OperatorTestCase.assertEqual(operator.abs(1), 1)

OperatorTestCase = test_operator.OperatorTestCase()
test_abs()
