import unittest
from operator import eq, le, ne
from abc import ABCMeta
import test_binop

def test_sub():
    RatTestCase.assertEqual(test_binop.Rat(7, 2) - test_binop.Rat(7, 5), test_binop.Rat(21, 10))
    RatTestCase.assertEqual(test_binop.Rat(7, 5) - 1, test_binop.Rat(2, 5))
    RatTestCase.assertEqual(1 - test_binop.Rat(3, 5), test_binop.Rat(2, 5))
    RatTestCase.assertEqual(test_binop.Rat(3, 2) - 1.0, 0.5)
    RatTestCase.assertEqual(1.0 - test_binop.Rat(1, 2), 0.5)

RatTestCase = test_binop.RatTestCase()
test_sub()
