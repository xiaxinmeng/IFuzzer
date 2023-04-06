import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_countOf():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.countOf)
    OperatorTestCase.assertRaises(TypeError, operator.countOf, None, None)
    OperatorTestCase.assertRaises(ZeroDivisionError, operator.countOf, BadIterable(), 1)
    OperatorTestCase.assertEqual(operator.countOf([1, 2, 1, 3, 1, 4], 3), 1)
    OperatorTestCase.assertEqual(operator.countOf([1, 2, 1, 3, 1, 4], 5), 0)

OperatorTestCase = test_operator.OperatorTestCase()
test_countOf()
