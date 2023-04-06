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

def test_fractions():
    from fractions import Fraction
    fraction_examples = [(Fraction(1, 100000000) + 1, Fraction(1)), (Fraction(100000001), Fraction(100000000)), (Fraction(10 ** 8 + 1, 10 ** 28), Fraction(1, 10 ** 20))]
    IsCloseTests.assertAllClose(fraction_examples, rel_tol=1e-08)
    IsCloseTests.assertAllNotClose(fraction_examples, rel_tol=1e-09)

IsCloseTests = test_math.IsCloseTests()
test_fractions()
