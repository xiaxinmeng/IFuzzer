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

def test_getformat():
    FormatFunctionsTestCase.assertIn(float.__getformat__('double'), ['unknown', 'IEEE, big-endian', 'IEEE, little-endian'])
    FormatFunctionsTestCase.assertIn(float.__getformat__('float'), ['unknown', 'IEEE, big-endian', 'IEEE, little-endian'])
    FormatFunctionsTestCase.assertRaises(ValueError, float.__getformat__, 'chicken')
    FormatFunctionsTestCase.assertRaises(TypeError, float.__getformat__, 1)

FormatFunctionsTestCase = test_float.FormatFunctionsTestCase()
test_getformat()
