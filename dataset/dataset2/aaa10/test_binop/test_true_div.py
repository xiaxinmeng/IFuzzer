import unittest
from operator import eq, le, ne
from abc import ABCMeta
import test_binop

def test_true_div():
    RatTestCase.assertEqual(test_binop.Rat(10, 3) / test_binop.Rat(5, 7), test_binop.Rat(14, 3))
    RatTestCase.assertEqual(test_binop.Rat(10, 3) / 3, test_binop.Rat(10, 9))
    RatTestCase.assertEqual(2 / test_binop.Rat(5), test_binop.Rat(2, 5))
    RatTestCase.assertEqual(3.0 * test_binop.Rat(1, 2), 1.5)
    RatTestCase.assertEqual(test_binop.Rat(1, 2) * 3.0, 1.5)
    RatTestCase.assertEqual(eval('1/2'), 0.5)

RatTestCase = test_binop.RatTestCase()
test_true_div()
