import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

def test_hash():
    for x in range(-30, 30):
        ComplexTest.assertEqual(hash(x), hash(complex(x, 0)))
        x /= 3.0
        ComplexTest.assertEqual(hash(x), hash(complex(x, 0.0)))

ComplexTest = test_complex.ComplexTest()
test_hash()
