import bisect
import collections
import collections.abc
import copy
import decimal
import doctest
import math
import pickle
import random
import sys
import unittest
from test import support
from test.support import import_helper
from decimal import Decimal
from fractions import Fraction
import statistics
import test_statistics

def test_float_zeroes():
    nzero = math.copysign(0.0, -1)
    ApproxEqualSpecialsTest.assertTrue(test_statistics.approx_equal(nzero, 0.0, tol=0.1, rel=0.1))

ApproxEqualSpecialsTest = test_statistics.ApproxEqualSpecialsTest()
test_float_zeroes()
