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

def test_identical():
    identical_examples = [(2.0, 2.0), (1e+199, 1e+199), (1.123e-300, 1.123e-300), (12345, 12345.0), (0.0, -0.0), (345678, 345678)]
    IsCloseTests.assertAllClose(identical_examples, rel_tol=0.0, abs_tol=0.0)

IsCloseTests = test_math.IsCloseTests()
test_identical()
