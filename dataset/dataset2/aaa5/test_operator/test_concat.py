import unittest
import pickle
import sys
from test import support
from test.support import import_helper
import test_operator

def test_concat():
    operator = OperatorTestCase.module
    OperatorTestCase.assertRaises(TypeError, operator.concat)
    OperatorTestCase.assertRaises(TypeError, operator.concat, None, None)
    OperatorTestCase.assertEqual(operator.concat('py', 'thon'), 'python')
    OperatorTestCase.assertEqual(operator.concat([1, 2], [3, 4]), [1, 2, 3, 4])
    OperatorTestCase.assertEqual(operator.concat(Seq1([5, 6]), Seq1([7])), [5, 6, 7])
    OperatorTestCase.assertEqual(operator.concat(Seq2([5, 6]), Seq2([7])), [5, 6, 7])
    OperatorTestCase.assertRaises(TypeError, operator.concat, 13, 29)

OperatorTestCase = test_operator.OperatorTestCase()
test_concat()
