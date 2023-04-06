import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_mul():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.mul)
    OperatorTestCase.assertRaises(TypeError, operator.mul, None, None)
    OperatorTestCase.assertEqual(operator.mul(5, 2), 10)

OperatorTestCase = test_operator.OperatorTestCase()
test_mul()
