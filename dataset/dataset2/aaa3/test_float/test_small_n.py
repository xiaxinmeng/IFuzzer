import fractions
import operator
import os
import random
import sys
import struct
import time
import unittest
from test import support
from test.test_grammar import VALID_UNDERSCORE_LITERALS, INVALID_UNDERSCORE_LITERALS
from math import isinf, isnan, copysign, ldexp
from array import array
import locale
from _testcapi import FLT_MAX
import random
import test_float

def test_small_n():
    for n in [-308, -309, -400, 1 - 2 ** 31, -2 ** 31, -2 ** 31 - 1, -2 ** 100]:
        RoundTestCase.assertEqual(round(123.456, n), 0.0)
        RoundTestCase.assertEqual(round(-123.456, n), -0.0)
        RoundTestCase.assertEqual(round(1e+300, n), 0.0)
        RoundTestCase.assertEqual(round(1e-320, n), 0.0)

RoundTestCase = test_float.RoundTestCase()
test_small_n()
