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

@support.requires_IEEE_754
def test_float_specials_do_unpack():
    for (fmt, data) in [('>f', test_float.BE_FLOAT_INF), ('>f', test_float.BE_FLOAT_NAN), ('<f', test_float.LE_FLOAT_INF), ('<f', test_float.LE_FLOAT_NAN)]:
        struct.unpack(fmt, data)

IEEEFormatTestCase = test_float.IEEEFormatTestCase()
test_float_specials_do_unpack()
