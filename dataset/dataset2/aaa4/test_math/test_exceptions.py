from test.support import run_unittest, verbose, requires_IEEE_754
from test import support
import unittest
import itertools
import decimal
import math
import os
import platform
import random
import struct
import sys
from sys import float_info
from random import random, gauss, shuffle
from decimal import Decimal
from fractions import Fraction
from decimal import Decimal as D
from fractions import Fraction as F
from fractions import Fraction
from decimal import Decimal
from fractions import Fraction
from doctest import DocFileSuite
import test_math

@unittest.skipUnless(verbose, 'requires verbose mode')
def test_exceptions():
    try:
        x = math.exp(-1000000000)
    except:
        MathTests.fail('underflowing exp() should not have raised an exception')
    if x != 0:
        MathTests.fail('underflowing exp() should have returned 0')
    try:
        x = math.exp(1000000000)
    except OverflowError:
        pass
    else:
        MathTests.fail("overflowing exp() didn't trigger OverflowError")
    try:
        x = math.sqrt(-1.0)
    except ValueError:
        pass
    else:
        MathTests.fail("sqrt(-1) didn't raise ValueError")

MathTests = test_math.MathTests()
test_exceptions()
