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

def test_ends():
    HexFloatTestCase.identical(HexFloatTestCase.MIN, ldexp(1.0, -1022))
    HexFloatTestCase.identical(HexFloatTestCase.TINY, ldexp(1.0, -1074))
    HexFloatTestCase.identical(HexFloatTestCase.EPS, ldexp(1.0, -52))
    HexFloatTestCase.identical(HexFloatTestCase.MAX, 2.0 * (ldexp(1.0, 1023) - ldexp(1.0, 970)))

HexFloatTestCase = test_float.HexFloatTestCase()
test_ends()
