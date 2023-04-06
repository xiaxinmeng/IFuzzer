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

def test_invalid_inputs():
    invalid_inputs = ['infi', '-Infinit', '++inf', '-+Inf', '--nan', '+-NaN', 'snan', 'NaNs', 'nna', 'an', 'nf', 'nfinity', 'inity', 'iinity', '0xnan', '', ' ', 'x1.0p0', '0xX1.0p0', '+ 0x1.0p0', '- 0x1.0p0', '0 x1.0p0', '0x 1.0p0', '0x1 2.0p0', '+0x1 .0p0', '0x1. 0p0', '-0x1.0 1p0', '-0x1.0 p0', '+0x1.0p +0', '0x1.0p -0', '0x1.0p 0', '+0x1.0p+ 0', '-0x1.0p- 0', '++0x1.0p-0', '--0x1.0p0', '+-0x1.0p+0', '-+0x1.0p0', '0x1.0p++0', '+0x1.0p+-0', '-0x1.0p-+0', '0x1.0p--0', '0x1.0.p0', '0x.p0', '0x1,p0', '0x1pa', '0x1p０', '０x1p0', '0x１p0', '0x1.０p0', '0x1p0 \n 0x2p0', '0x1p0\x00 0x1p0']
    for x in invalid_inputs:
        try:
            result = test_float.fromHex(x)
        except ValueError:
            pass
        else:
            HexFloatTestCase.fail('Expected float.fromhex(%r) to raise ValueError; got %r instead' % (x, result))

HexFloatTestCase = test_float.HexFloatTestCase()
test_invalid_inputs()
