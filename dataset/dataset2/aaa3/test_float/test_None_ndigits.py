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

def test_None_ndigits():
    for x in (round(1.23), round(1.23, None), round(1.23, ndigits=None)):
        RoundTestCase.assertEqual(x, 1)
        RoundTestCase.assertIsInstance(x, int)
    for x in (round(1.78), round(1.78, None), round(1.78, ndigits=None)):
        RoundTestCase.assertEqual(x, 2)
        RoundTestCase.assertIsInstance(x, int)

RoundTestCase = test_float.RoundTestCase()
test_None_ndigits()
