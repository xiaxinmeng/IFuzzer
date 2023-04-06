import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_lshift():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.lshift)
    OperatorTestCase.assertRaises(TypeError, operator.lshift, None, 42)
    OperatorTestCase.assertEqual(operator.lshift(5, 1), 10)
    OperatorTestCase.assertEqual(operator.lshift(5, 0), 5)
    OperatorTestCase.assertRaises(ValueError, operator.lshift, 2, -1)

OperatorTestCase = test_operator.OperatorTestCase()
test_lshift()
