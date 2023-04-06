import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

def test_conjugate():
    ComplexTest.assertClose(complex(5.3, 9.8).conjugate(), 5.3 - 9.8j)

ComplexTest = test_complex.ComplexTest()
test_conjugate()
