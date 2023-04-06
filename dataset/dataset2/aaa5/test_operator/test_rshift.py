import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_rshift():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.rshift)
    OperatorTestCase.assertRaises(TypeError, operator.rshift, None, 42)
    OperatorTestCase.assertEqual(operator.rshift(5, 1), 2)
    OperatorTestCase.assertEqual(operator.rshift(5, 0), 5)
    OperatorTestCase.assertRaises(ValueError, operator.rshift, 2, -1)

OperatorTestCase = test_operator.OperatorTestCase()
test_rshift()
