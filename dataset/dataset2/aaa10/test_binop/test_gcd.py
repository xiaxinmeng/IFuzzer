import unittest
from operator import eq, le, ne
from abc import ABCMeta
import test_binop

def test_gcd():
    RatTestCase.assertEqual(test_binop.gcd(10, 12), 2)
    RatTestCase.assertEqual(test_binop.gcd(10, 15), 5)
    RatTestCase.assertEqual(test_binop.gcd(10, 11), 1)
    RatTestCase.assertEqual(test_binop.gcd(100, 15), 5)
    RatTestCase.assertEqual(test_binop.gcd(-10, 2), -2)
    RatTestCase.assertEqual(test_binop.gcd(10, -2), 2)
    RatTestCase.assertEqual(test_binop.gcd(-10, -2), -2)
    for i in range(1, 20):
        for j in range(1, 20):
            RatTestCase.assertTrue(test_binop.gcd(i, j) > 0)
            RatTestCase.assertTrue(test_binop.gcd(-i, j) < 0)
            RatTestCase.assertTrue(test_binop.gcd(i, -j) > 0)
            RatTestCase.assertTrue(test_binop.gcd(-i, -j) < 0)

RatTestCase = test_binop.RatTestCase()
test_gcd()
