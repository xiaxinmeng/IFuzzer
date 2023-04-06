import unittest
from operator import eq, le, ne
from abc import ABCMeta
import test_binop

def test_floordiv():
    RatTestCase.assertEqual(test_binop.Rat(10) // test_binop.Rat(4), 2)
    RatTestCase.assertEqual(test_binop.Rat(10, 3) // test_binop.Rat(4, 3), 2)
    RatTestCase.assertEqual(test_binop.Rat(10) // 4, 2)
    RatTestCase.assertEqual(10 // test_binop.Rat(4), 2)

RatTestCase = test_binop.RatTestCase()
test_floordiv()
