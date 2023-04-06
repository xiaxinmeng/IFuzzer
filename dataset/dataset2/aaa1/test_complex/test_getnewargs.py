import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from random import random
from math import atan2, isnan, copysign
import operator
import test_complex

def test_getnewargs():
    ComplexTest.assertEqual((1 + 2j).__getnewargs__(), (1.0, 2.0))
    ComplexTest.assertEqual((1 - 2j).__getnewargs__(), (1.0, -2.0))
    ComplexTest.assertEqual(2j.__getnewargs__(), (0.0, 2.0))
    ComplexTest.assertEqual((-0j).__getnewargs__(), (0.0, -0.0))
    ComplexTest.assertEqual(complex(0, test_complex.INF).__getnewargs__(), (0.0, test_complex.INF))
    ComplexTest.assertEqual(complex(test_complex.INF, 0).__getnewargs__(), (test_complex.INF, 0.0))

ComplexTest = test_complex.ComplexTest()
test_getnewargs()
