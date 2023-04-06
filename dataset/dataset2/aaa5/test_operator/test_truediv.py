import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_truediv():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.truediv, 5)
    OperatorTestCase.assertRaises(TypeError, operator.truediv, None, None)
    OperatorTestCase.assertEqual(operator.truediv(5, 2), 2.5)

OperatorTestCase = test_operator.OperatorTestCase()
test_truediv()
