import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

@support.requires_IEEE_754
def test_overflow():
    ComplexTest.assertEqual(complex('1e500'), complex(test_complex.INF, 0.0))
    ComplexTest.assertEqual(complex('-1e500j'), complex(0.0, -test_complex.INF))
    ComplexTest.assertEqual(complex('-1e500+1.8e308j'), complex(-test_complex.INF, test_complex.INF))

ComplexTest = test_complex.ComplexTest()
test_overflow()
