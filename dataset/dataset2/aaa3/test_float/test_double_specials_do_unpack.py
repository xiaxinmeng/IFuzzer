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
def test_double_specials_do_unpack():
    for (fmt, data) in [('>d', test_float.BE_DOUBLE_INF), ('>d', test_float.BE_DOUBLE_NAN), ('<d', test_float.LE_DOUBLE_INF), ('<d', test_float.LE_DOUBLE_NAN)]:
        struct.unpack(fmt, data)

IEEEFormatTestCase = test_float.IEEEFormatTestCase()
test_double_specials_do_unpack()
