import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

@support.requires_IEEE_754
def test_plus_minus_0j():
    (z1, z2) = (0j, -0j)
    ComplexTest.assertEqual(atan2(z1.imag, -1.0), atan2(0.0, -1.0))
    ComplexTest.assertEqual(atan2(z2.imag, -1.0), atan2(-0.0, -1.0))

ComplexTest = test_complex.ComplexTest()
test_plus_minus_0j()
