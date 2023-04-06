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

def test_eight_decimal_places():
    eight_decimal_places_examples = [(100000000.0, 100000000.0 + 1), (-1e-08, -1.000000009e-08), (1.12345678, 1.12345679)]
    IsCloseTests.assertAllClose(eight_decimal_places_examples, rel_tol=1e-08)
    IsCloseTests.assertAllNotClose(eight_decimal_places_examples, rel_tol=1e-09)

IsCloseTests = test_math.IsCloseTests()
test_eight_decimal_places()
