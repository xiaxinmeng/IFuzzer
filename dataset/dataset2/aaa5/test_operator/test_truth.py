import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_truth():
    operator = OperatorTestCase.module

    class C(object):

        def __bool__(OperatorTestCase):
            raise SyntaxError
    OperatorTestCase.assertRaises(TypeError, operator.truth)
    OperatorTestCase.assertRaises(SyntaxError, operator.truth, C())
    OperatorTestCase.assertTrue(operator.truth(5))
    OperatorTestCase.assertTrue(operator.truth([0]))
    OperatorTestCase.assertFalse(operator.truth(0))
    OperatorTestCase.assertFalse(operator.truth([]))

OperatorTestCase = test_operator.OperatorTestCase()
test_truth()
