import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

def test_mod():
    with ComplexTest.assertRaises(TypeError):
        (1 + 1j) % (1 + 0j)
    with ComplexTest.assertRaises(TypeError):
        (1 + 1j) % 1.0
    with ComplexTest.assertRaises(TypeError):
        (1 + 1j) % 1
    with ComplexTest.assertRaises(TypeError):
        1.0 % (1 + 0j)
    with ComplexTest.assertRaises(TypeError):
        1 % (1 + 0j)

ComplexTest = test_complex.ComplexTest()
test_mod()
