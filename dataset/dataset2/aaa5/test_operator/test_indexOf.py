import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_indexOf():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.indexOf)
    OperatorTestCase.assertRaises(TypeError, operator.indexOf, None, None)
    OperatorTestCase.assertRaises(ZeroDivisionError, operator.indexOf, BadIterable(), 1)
    OperatorTestCase.assertEqual(operator.indexOf([4, 3, 2, 1], 3), 1)
    OperatorTestCase.assertRaises(ValueError, operator.indexOf, [4, 3, 2, 1], 0)

OperatorTestCase = test_operator.OperatorTestCase()
test_indexOf()
