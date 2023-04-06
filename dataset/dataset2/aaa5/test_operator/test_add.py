import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_add():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.add)
    OperatorTestCase.assertRaises(TypeError, operator.add, None, None)
    OperatorTestCase.assertEqual(operator.add(3, 4), 7)

OperatorTestCase = test_operator.OperatorTestCase()
test_add()
