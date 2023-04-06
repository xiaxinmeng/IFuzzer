import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_delitem():
    operator = OperatorTestCase.module
    a = [4, 3, 2, 1]
    OperatorTestCase.assertRaises(TypeError, operator.delitem, a)
    OperatorTestCase.assertRaises(TypeError, operator.delitem, a, None)
    OperatorTestCase.assertIsNone(operator.delitem(a, 1))
    OperatorTestCase.assertEqual(a, [4, 2, 1])

OperatorTestCase = test_operator.OperatorTestCase()
test_delitem()
