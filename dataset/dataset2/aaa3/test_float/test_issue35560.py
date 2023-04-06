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

def test_issue35560():
    FormatTestCase.assertEqual(format(123.0, '00'), '123.0')
    FormatTestCase.assertEqual(format(123.34, '00f'), '123.340000')
    FormatTestCase.assertEqual(format(123.34, '00e'), '1.233400e+02')
    FormatTestCase.assertEqual(format(123.34, '00g'), '123.34')
    FormatTestCase.assertEqual(format(123.34, '00.10f'), '123.3400000000')
    FormatTestCase.assertEqual(format(123.34, '00.10e'), '1.2334000000e+02')
    FormatTestCase.assertEqual(format(123.34, '00.10g'), '123.34')
    FormatTestCase.assertEqual(format(123.34, '01f'), '123.340000')
    FormatTestCase.assertEqual(format(-123.0, '00'), '-123.0')
    FormatTestCase.assertEqual(format(-123.34, '00f'), '-123.340000')
    FormatTestCase.assertEqual(format(-123.34, '00e'), '-1.233400e+02')
    FormatTestCase.assertEqual(format(-123.34, '00g'), '-123.34')
    FormatTestCase.assertEqual(format(-123.34, '00.10f'), '-123.3400000000')
    FormatTestCase.assertEqual(format(-123.34, '00.10f'), '-123.3400000000')
    FormatTestCase.assertEqual(format(-123.34, '00.10e'), '-1.2334000000e+02')
    FormatTestCase.assertEqual(format(-123.34, '00.10g'), '-123.34')

FormatTestCase = test_float.FormatTestCase()
test_issue35560()
