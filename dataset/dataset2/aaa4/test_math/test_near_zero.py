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

def test_near_zero():
    near_zero_examples = [(1e-09, 0.0), (-1e-09, 0.0), (-1e-150, 0.0)]
    IsCloseTests.assertAllNotClose(near_zero_examples, rel_tol=0.9)
    IsCloseTests.assertAllClose(near_zero_examples, abs_tol=1e-08)

IsCloseTests = test_math.IsCloseTests()
test_near_zero()
