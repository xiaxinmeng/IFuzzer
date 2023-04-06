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

def test_overflow():
    RoundTestCase.assertRaises(OverflowError, round, 1.6e+308, -308)
    RoundTestCase.assertRaises(OverflowError, round, -1.7e+308, -308)

RoundTestCase = test_float.RoundTestCase()
test_overflow()
