import unittest
from operator import eq, le, ne
from abc import ABCMeta
import test_binop

def test_mul():
    RatTestCase.assertEqual(test_binop.Rat(2, 3) * test_binop.Rat(5, 7), test_binop.Rat(10, 21))
    RatTestCase.assertEqual(test_binop.Rat(10, 3) * 3, 10)
    RatTestCase.assertEqual(3 * test_binop.Rat(10, 3), 10)
    RatTestCase.assertEqual(test_binop.Rat(10, 5) * 0.5, 1.0)
    RatTestCase.assertEqual(0.5 * test_binop.Rat(10, 5), 1.0)

RatTestCase = test_binop.RatTestCase()
test_mul()
