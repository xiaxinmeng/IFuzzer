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

def test_float_memoryview():
    GeneralFloatCases.assertEqual(float(memoryview(b'12.3')[1:4]), 2.3)
    GeneralFloatCases.assertEqual(float(memoryview(b'12.3\x00')[1:4]), 2.3)
    GeneralFloatCases.assertEqual(float(memoryview(b'12.3 ')[1:4]), 2.3)
    GeneralFloatCases.assertEqual(float(memoryview(b'12.3A')[1:4]), 2.3)
    GeneralFloatCases.assertEqual(float(memoryview(b'12.34')[1:4]), 2.3)

GeneralFloatCases = test_float.GeneralFloatCases()
test_float_memoryview()
