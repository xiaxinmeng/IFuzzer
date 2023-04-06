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

def test_identical_infinite():
    IsCloseTests.assertIsClose(test_math.INF, test_math.INF)
    IsCloseTests.assertIsClose(test_math.INF, test_math.INF, abs_tol=0.0)
    IsCloseTests.assertIsClose(test_math.NINF, test_math.NINF)
    IsCloseTests.assertIsClose(test_math.NINF, test_math.NINF, abs_tol=0.0)

IsCloseTests = test_math.IsCloseTests()
test_identical_infinite()
