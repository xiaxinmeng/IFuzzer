import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_bitwise_xor():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.xor)
    OperatorTestCase.assertRaises(TypeError, operator.xor, None, None)
    OperatorTestCase.assertEqual(operator.xor(11, 12), 7)

OperatorTestCase = test_operator.OperatorTestCase()
test_bitwise_xor()
