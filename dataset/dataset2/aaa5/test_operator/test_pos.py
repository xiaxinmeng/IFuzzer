import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_pos():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.pos)
    OperatorTestCase.assertRaises(TypeError, operator.pos, None)
    OperatorTestCase.assertEqual(operator.pos(5), 5)
    OperatorTestCase.assertEqual(operator.pos(-5), -5)
    OperatorTestCase.assertEqual(operator.pos(0), 0)
    OperatorTestCase.assertEqual(operator.pos(-0), 0)

OperatorTestCase = test_operator.OperatorTestCase()
test_pos()
