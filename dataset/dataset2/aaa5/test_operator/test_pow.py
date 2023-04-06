import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_pow():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.pow)
    OperatorTestCase.assertRaises(TypeError, operator.pow, None, None)
    OperatorTestCase.assertEqual(operator.pow(3, 5), 3 ** 5)
    OperatorTestCase.assertRaises(TypeError, operator.pow, 1)
    OperatorTestCase.assertRaises(TypeError, operator.pow, 1, 2, 3)

OperatorTestCase = test_operator.OperatorTestCase()
test_pow()
