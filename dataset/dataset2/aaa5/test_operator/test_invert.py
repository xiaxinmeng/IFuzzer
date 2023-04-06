import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_invert():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.invert)
    OperatorTestCase.assertRaises(TypeError, operator.invert, None)
    OperatorTestCase.assertEqual(operator.inv(4), -5)

OperatorTestCase = test_operator.OperatorTestCase()
test_invert()
