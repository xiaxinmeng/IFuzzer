import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_sub():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.sub)
    OperatorTestCase.assertRaises(TypeError, operator.sub, None, None)
    OperatorTestCase.assertEqual(operator.sub(5, 2), 3)

OperatorTestCase = test_operator.OperatorTestCase()
test_sub()
