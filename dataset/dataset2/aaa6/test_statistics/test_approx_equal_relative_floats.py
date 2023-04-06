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

def test_approx_equal_relative_floats():
    for x in [-178.34, -0.1, 0.1, 1.0, 36.97, 2847.136, 9145.074]:
        ApproxEqualInexactTest.do_approx_equal_rel_test(x, 0.02)
        ApproxEqualInexactTest.do_approx_equal_rel_test(x, 0.0001)

ApproxEqualInexactTest = test_statistics.ApproxEqualInexactTest()
test_approx_equal_relative_floats()
