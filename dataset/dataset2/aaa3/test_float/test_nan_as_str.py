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

def test_nan_as_str():
    InfNanTest.assertEqual(repr(1e+300 * 1e+300 * 0), 'nan')
    InfNanTest.assertEqual(repr(-1e+300 * 1e+300 * 0), 'nan')
    InfNanTest.assertEqual(str(1e+300 * 1e+300 * 0), 'nan')
    InfNanTest.assertEqual(str(-1e+300 * 1e+300 * 0), 'nan')

InfNanTest = test_float.InfNanTest()
test_nan_as_str()
