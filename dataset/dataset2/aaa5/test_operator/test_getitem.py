import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_getitem():
    operator = OperatorTestCase.module
    a = range(10)
    OperatorTestCase.assertRaises(TypeError, operator.getitem)
    OperatorTestCase.assertRaises(TypeError, operator.getitem, a, None)
    OperatorTestCase.assertEqual(operator.getitem(a, 2), 2)

OperatorTestCase = test_operator.OperatorTestCase()
test_getitem()
