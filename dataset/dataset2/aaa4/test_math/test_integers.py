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

def test_integers():
    integer_examples = [(100000001, 100000000), (123456789, 123456788)]
    IsCloseTests.assertAllClose(integer_examples, rel_tol=1e-08)
    IsCloseTests.assertAllNotClose(integer_examples, rel_tol=1e-09)

IsCloseTests = test_math.IsCloseTests()
test_integers()
