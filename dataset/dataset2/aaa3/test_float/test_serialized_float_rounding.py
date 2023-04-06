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
def test_serialized_float_rounding():
    from _testcapi import FLT_MAX
    IEEEFormatTestCase.assertEqual(struct.pack('<f', 3.40282356e+38), struct.pack('<f', FLT_MAX))
    IEEEFormatTestCase.assertEqual(struct.pack('<f', -3.40282356e+38), struct.pack('<f', -FLT_MAX))

IEEEFormatTestCase = test_float.IEEEFormatTestCase()
test_serialized_float_rounding()
