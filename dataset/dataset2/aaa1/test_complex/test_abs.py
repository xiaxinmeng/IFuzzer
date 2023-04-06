import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

def test_abs():
    nums = [complex(x / 3.0, y / 7.0) for x in range(-9, 9) for y in range(-9, 9)]
    for num in nums:
        ComplexTest.assertAlmostEqual((num.real ** 2 + num.imag ** 2) ** 0.5, abs(num))

ComplexTest = test_complex.ComplexTest()
test_abs()
