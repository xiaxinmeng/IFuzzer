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

def test_float_specials_dont_unpack():
    for (fmt, data) in [('>f', test_float.BE_FLOAT_INF), ('>f', test_float.BE_FLOAT_NAN), ('<f', test_float.LE_FLOAT_INF), ('<f', test_float.LE_FLOAT_NAN)]:
        UnknownFormatTestCase.assertRaises(ValueError, struct.unpack, fmt, data)

UnknownFormatTestCase = test_float.UnknownFormatTestCase()
test_float_specials_dont_unpack()
