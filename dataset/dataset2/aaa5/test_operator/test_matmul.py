import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_matmul():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.matmul)
    OperatorTestCase.assertRaises(TypeError, operator.matmul, 42, 42)

    class M:

        def __matmul__(OperatorTestCase, other):
            return other - 1
    OperatorTestCase.assertEqual(M() @ 42, 41)

OperatorTestCase = test_operator.OperatorTestCase()
test_matmul()
