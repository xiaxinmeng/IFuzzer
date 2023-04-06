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

def test_approx_equal_absolute_floats():
    for x in [-284.126, -97.1, -3.4, -2.15, 0.5, 1.0, 7.8, 4.23, 3817.4]:
        ApproxEqualInexactTest.do_approx_equal_abs_test(x, 1.5)
        ApproxEqualInexactTest.do_approx_equal_abs_test(x, 0.01)
        ApproxEqualInexactTest.do_approx_equal_abs_test(x, 0.0001)

ApproxEqualInexactTest = test_statistics.ApproxEqualInexactTest()
test_approx_equal_absolute_floats()
