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

@requires_IEEE_754
def test_ulp():
    MathTests.assertEqual(math.ulp(1.0), sys.float_info.epsilon)
    MathTests.assertEqual(math.ulp(2 ** 52), 1.0)
    MathTests.assertEqual(math.ulp(2 ** 53), 2.0)
    MathTests.assertEqual(math.ulp(2 ** 64), 4096.0)
    MathTests.assertEqual(math.ulp(0.0), sys.float_info.min * sys.float_info.epsilon)
    MathTests.assertEqual(math.ulp(test_math.FLOAT_MAX), test_math.FLOAT_MAX - math.nextafter(test_math.FLOAT_MAX, -test_math.INF))
    MathTests.assertEqual(math.ulp(test_math.INF), test_math.INF)
    MathTests.assertIsNaN(math.ulp(math.nan))
    for x in (0.0, 1.0, 2 ** 52, 2 ** 64, test_math.INF):
        with MathTests.subTest(x=x):
            MathTests.assertEqual(math.ulp(-x), math.ulp(x))

MathTests = test_math.MathTests()
test_ulp()
