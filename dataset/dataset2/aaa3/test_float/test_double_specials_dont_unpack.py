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

def test_double_specials_dont_unpack():
    for (fmt, data) in [('>d', test_float.BE_DOUBLE_INF), ('>d', test_float.BE_DOUBLE_NAN), ('<d', test_float.LE_DOUBLE_INF), ('<d', test_float.LE_DOUBLE_NAN)]:
        UnknownFormatTestCase.assertRaises(ValueError, struct.unpack, fmt, data)

UnknownFormatTestCase = test_float.UnknownFormatTestCase()
test_double_specials_dont_unpack()
