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

def test_approx_equal_absolute_decimals():
    delta = Decimal('0.01')
    for d in map(Decimal, '1.0 3.5 36.08 61.79 7912.3648'.split()):
        ApproxEqualInexactTest.do_approx_equal_abs_test(d, delta)
        ApproxEqualInexactTest.do_approx_equal_abs_test(-d, delta)

ApproxEqualInexactTest = test_statistics.ApproxEqualInexactTest()
test_approx_equal_absolute_decimals()
