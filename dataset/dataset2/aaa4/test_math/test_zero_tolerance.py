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

def test_zero_tolerance():
    zero_tolerance_close_examples = [(1.0, 1.0), (-3.4, -3.4), (-1e-300, -1e-300)]
    IsCloseTests.assertAllClose(zero_tolerance_close_examples, rel_tol=0.0)
    zero_tolerance_not_close_examples = [(1.0, 1.000000000000001), (0.99999999999999, 1.0), (1e+200, 9.99999999999999e+199)]
    IsCloseTests.assertAllNotClose(zero_tolerance_not_close_examples, rel_tol=0.0)

IsCloseTests = test_math.IsCloseTests()
test_zero_tolerance()
