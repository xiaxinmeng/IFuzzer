import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

@support.requires_IEEE_754
def test_negated_imaginary_literal():
    z0 = -0j
    z1 = -7j
    z2 = -1e309j
    ComplexTest.assertFloatsAreIdentical(z0.real, -0.0)
    ComplexTest.assertFloatsAreIdentical(z0.imag, -0.0)
    ComplexTest.assertFloatsAreIdentical(z1.real, -0.0)
    ComplexTest.assertFloatsAreIdentical(z1.imag, -7.0)
    ComplexTest.assertFloatsAreIdentical(z2.real, -0.0)
    ComplexTest.assertFloatsAreIdentical(z2.imag, -test_complex.INF)

ComplexTest = test_complex.ComplexTest()
test_negated_imaginary_literal()
