import math
import operator
import unittest
from numbers import Complex, Real, Rational, Integral
import test_abstract_numbers

def test_float():
    TestNumbers.assertFalse(issubclass(float, Rational))
    TestNumbers.assertTrue(issubclass(float, Real))
    TestNumbers.assertEqual(7.3, float(7.3).real)
    TestNumbers.assertEqual(0, float(7.3).imag)
    TestNumbers.assertEqual(7.3, float(7.3).conjugate())
    TestNumbers.assertEqual(-7.3, float(-7.3).conjugate())

TestNumbers = test_abstract_numbers.TestNumbers()
test_float()
