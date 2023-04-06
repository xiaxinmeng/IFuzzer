import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_floordiv():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.floordiv, 5)
    OperatorTestCase.assertRaises(TypeError, operator.floordiv, None, None)
    OperatorTestCase.assertEqual(operator.floordiv(5, 2), 2)

OperatorTestCase = test_operator.OperatorTestCase()
test_floordiv()
