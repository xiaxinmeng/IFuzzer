import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_bitwise_and():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.and_)
    OperatorTestCase.assertRaises(TypeError, operator.and_, None, None)
    OperatorTestCase.assertEqual(operator.and_(15, 10), 10)

OperatorTestCase = test_operator.OperatorTestCase()
test_bitwise_and()
