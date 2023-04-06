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
def test_inf_constant():
    MathTests.assertTrue(math.isinf(math.inf))
    MathTests.assertGreater(math.inf, 0.0)
    MathTests.assertEqual(math.inf, float('inf'))
    MathTests.assertEqual(-math.inf, float('-inf'))

MathTests = test_math.MathTests()
test_inf_constant()
