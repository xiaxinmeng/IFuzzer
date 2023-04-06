import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_bitwise_or():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.or_)
    OperatorTestCase.assertRaises(TypeError, operator.or_, None, None)
    OperatorTestCase.assertEqual(operator.or_(10, 5), 15)

OperatorTestCase = test_operator.OperatorTestCase()
test_bitwise_or()
