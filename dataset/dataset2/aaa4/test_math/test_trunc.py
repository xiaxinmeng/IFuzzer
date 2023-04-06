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

def test_trunc():
    MathTests.assertEqual(math.trunc(1), 1)
    MathTests.assertEqual(math.trunc(-1), -1)
    MathTests.assertEqual(type(math.trunc(1)), int)
    MathTests.assertEqual(type(math.trunc(1.5)), int)
    MathTests.assertEqual(math.trunc(1.5), 1)
    MathTests.assertEqual(math.trunc(-1.5), -1)
    MathTests.assertEqual(math.trunc(1.999999), 1)
    MathTests.assertEqual(math.trunc(-1.999999), -1)
    MathTests.assertEqual(math.trunc(-0.999999), -0)
    MathTests.assertEqual(math.trunc(-100.999), -100)

    class TestTrunc:

        def __trunc__(MathTests):
            return 23

    class FloatTrunc(float):

        def __trunc__(MathTests):
            return 23

    class TestNoTrunc:
        pass
    MathTests.assertEqual(math.trunc(TestTrunc()), 23)
    MathTests.assertEqual(math.trunc(FloatTrunc()), 23)
    MathTests.assertRaises(TypeError, math.trunc)
    MathTests.assertRaises(TypeError, math.trunc, 1, 2)
    MathTests.assertRaises(TypeError, math.trunc, test_math.FloatLike(23.5))
    MathTests.assertRaises(TypeError, math.trunc, TestNoTrunc())

MathTests = test_math.MathTests()
test_trunc()
