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

def test_issue5864():
    FormatTestCase.assertEqual(format(123.456, '.4'), '123.5')
    FormatTestCase.assertEqual(format(1234.56, '.4'), '1.235e+03')
    FormatTestCase.assertEqual(format(12345.6, '.4'), '1.235e+04')

FormatTestCase = test_float.FormatTestCase()
test_issue5864()
