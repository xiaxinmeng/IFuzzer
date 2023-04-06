import math
import operator
import unittest
from numbers import Complex, Real, Rational, Integral
import test_abstract_numbers

def test_int():
    TestNumbers.assertTrue(issubclass(int, Integral))
    TestNumbers.assertTrue(issubclass(int, Complex))
    TestNumbers.assertEqual(7, int(7).real)
    TestNumbers.assertEqual(0, int(7).imag)
    TestNumbers.assertEqual(7, int(7).conjugate())
    TestNumbers.assertEqual(-7, int(-7).conjugate())
    TestNumbers.assertEqual(7, int(7).numerator)
    TestNumbers.assertEqual(1, int(7).denominator)

TestNumbers = test_abstract_numbers.TestNumbers()
test_int()
