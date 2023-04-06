import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_neg():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.neg)
    OperatorTestCase.assertRaises(TypeError, operator.neg, None)
    OperatorTestCase.assertEqual(operator.neg(5), -5)
    OperatorTestCase.assertEqual(operator.neg(-5), 5)
    OperatorTestCase.assertEqual(operator.neg(0), 0)
    OperatorTestCase.assertEqual(operator.neg(-0), 0)

OperatorTestCase = test_operator.OperatorTestCase()
test_neg()
