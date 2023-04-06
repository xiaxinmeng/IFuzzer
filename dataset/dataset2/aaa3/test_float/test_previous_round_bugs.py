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

@unittest.skipUnless(getattr(sys, 'float_repr_style', '') == 'short', 'applies only when using short float repr style')
def test_previous_round_bugs():
    RoundTestCase.assertEqual(round(562949953421312.5, 1), 562949953421312.5)
    RoundTestCase.assertEqual(round(56294995342131.5, 3), 56294995342131.5)
    RoundTestCase.assertEqual(round(25.0, -1), 20.0)
    RoundTestCase.assertEqual(round(35.0, -1), 40.0)
    RoundTestCase.assertEqual(round(45.0, -1), 40.0)
    RoundTestCase.assertEqual(round(55.0, -1), 60.0)
    RoundTestCase.assertEqual(round(65.0, -1), 60.0)
    RoundTestCase.assertEqual(round(75.0, -1), 80.0)
    RoundTestCase.assertEqual(round(85.0, -1), 80.0)
    RoundTestCase.assertEqual(round(95.0, -1), 100.0)

RoundTestCase = test_float.RoundTestCase()
test_previous_round_bugs()
