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

def test_float_floor():
    GeneralFloatCases.assertIsInstance(float(0.5).__floor__(), int)
    GeneralFloatCases.assertEqual(float(0.5).__floor__(), 0)
    GeneralFloatCases.assertEqual(float(1.0).__floor__(), 1)
    GeneralFloatCases.assertEqual(float(1.5).__floor__(), 1)
    GeneralFloatCases.assertEqual(float(-0.5).__floor__(), -1)
    GeneralFloatCases.assertEqual(float(-1.0).__floor__(), -1)
    GeneralFloatCases.assertEqual(float(-1.5).__floor__(), -2)
    GeneralFloatCases.assertEqual(float(1.23e+167).__floor__(), 1.23e+167)
    GeneralFloatCases.assertEqual(float(-1.23e+167).__floor__(), -1.23e+167)
    GeneralFloatCases.assertRaises(ValueError, float('nan').__floor__)
    GeneralFloatCases.assertRaises(OverflowError, float('inf').__floor__)
    GeneralFloatCases.assertRaises(OverflowError, float('-inf').__floor__)

GeneralFloatCases = test_float.GeneralFloatCases()
test_float_floor()
