import unittest
from operator import eq, le, ne
from abc import ABCMeta
import test_binop

def test_eq():
    RatTestCase.assertEqual(test_binop.Rat(10), test_binop.Rat(20, 2))
    RatTestCase.assertEqual(test_binop.Rat(10), 10)
    RatTestCase.assertEqual(10, test_binop.Rat(10))
    RatTestCase.assertEqual(test_binop.Rat(10), 10.0)
    RatTestCase.assertEqual(10.0, test_binop.Rat(10))

RatTestCase = test_binop.RatTestCase()
test_eq()
