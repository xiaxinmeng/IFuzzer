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

def test_issue39871():

    class F:

        def __float__(MathTests):
            MathTests.converted = True
            1 / 0
    for func in (math.atan2, math.copysign, math.remainder):
        y = F()
        with MathTests.assertRaises(TypeError):
            func('not a number', y)
        MathTests.assertFalse(getattr(y, 'converted', False))

MathTests = test_math.MathTests()
test_issue39871()
