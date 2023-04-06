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

def test_inf_ninf_nan():
    not_close_examples = [(test_math.NAN, test_math.NAN), (test_math.NAN, 1e-100), (1e-100, test_math.NAN), (test_math.INF, test_math.NAN), (test_math.NAN, test_math.INF), (test_math.INF, test_math.NINF), (test_math.INF, 1.0), (1.0, test_math.INF), (test_math.INF, 1e+308), (1e+308, test_math.INF)]
    IsCloseTests.assertAllNotClose(not_close_examples, abs_tol=0.999999999999999)

IsCloseTests = test_math.IsCloseTests()
test_inf_ninf_nan()
