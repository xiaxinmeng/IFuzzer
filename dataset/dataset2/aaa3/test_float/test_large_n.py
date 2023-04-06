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

def test_large_n():
    for n in [324, 325, 400, 2 ** 31 - 1, 2 ** 31, 2 ** 32, 2 ** 100]:
        RoundTestCase.assertEqual(round(123.456, n), 123.456)
        RoundTestCase.assertEqual(round(-123.456, n), -123.456)
        RoundTestCase.assertEqual(round(1e+300, n), 1e+300)
        RoundTestCase.assertEqual(round(1e-320, n), 1e-320)
    RoundTestCase.assertEqual(round(1e+150, 300), 1e+150)
    RoundTestCase.assertEqual(round(1e+300, 307), 1e+300)
    RoundTestCase.assertEqual(round(-3.1415, 308), -3.1415)
    RoundTestCase.assertEqual(round(1e+150, 309), 1e+150)
    RoundTestCase.assertEqual(round(1.4e-315, 315), 1e-315)

RoundTestCase = test_float.RoundTestCase()
test_large_n()
