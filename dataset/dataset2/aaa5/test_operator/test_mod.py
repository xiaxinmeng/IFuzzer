import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_mod():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.mod)
    OperatorTestCase.assertRaises(TypeError, operator.mod, None, 42)
    OperatorTestCase.assertEqual(operator.mod(5, 2), 1)

OperatorTestCase = test_operator.OperatorTestCase()
test_mod()
