import unittest
from operator import eq, le, ne
from abc import ABCMeta
import test_binop

def test_add():
    RatTestCase.assertEqual(test_binop.Rat(2, 3) + test_binop.Rat(1, 3), 1)
    RatTestCase.assertEqual(test_binop.Rat(2, 3) + 1, test_binop.Rat(5, 3))
    RatTestCase.assertEqual(1 + test_binop.Rat(2, 3), test_binop.Rat(5, 3))
    RatTestCase.assertEqual(1.0 + test_binop.Rat(1, 2), 1.5)
    RatTestCase.assertEqual(test_binop.Rat(1, 2) + 1.0, 1.5)

RatTestCase = test_binop.RatTestCase()
test_add()
