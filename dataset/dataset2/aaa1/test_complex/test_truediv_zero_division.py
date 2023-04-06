import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

def test_truediv_zero_division():
    for (a, b) in test_complex.ZERO_DIVISION:
        with ComplexTest.assertRaises(ZeroDivisionError):
            a / b

ComplexTest = test_complex.ComplexTest()
test_truediv_zero_division()
