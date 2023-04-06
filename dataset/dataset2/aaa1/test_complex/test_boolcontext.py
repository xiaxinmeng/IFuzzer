import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

def test_boolcontext():
    for i in range(100):
        ComplexTest.assertTrue(complex(random() + 1e-06, random() + 1e-06))
    ComplexTest.assertTrue(not complex(0.0, 0.0))

ComplexTest = test_complex.ComplexTest()
test_boolcontext()
