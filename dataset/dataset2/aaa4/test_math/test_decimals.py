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

def test_decimals():
    from decimal import Decimal
    decimal_examples = [(Decimal('1.00000001'), Decimal('1.0')), (Decimal('1.00000001e-20'), Decimal('1.0e-20')), (Decimal('1.00000001e-100'), Decimal('1.0e-100')), (Decimal('1.00000001e20'), Decimal('1.0e20'))]
    IsCloseTests.assertAllClose(decimal_examples, rel_tol=1e-08)
    IsCloseTests.assertAllNotClose(decimal_examples, rel_tol=1e-09)

IsCloseTests = test_math.IsCloseTests()
test_decimals()
