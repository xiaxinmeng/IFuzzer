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

def test_approx_equal_absolute_ints():
    for n in [-10737, -1975, -7, -2, 0, 1, 9, 37, 423, 9874, 23789110]:
        ApproxEqualInexactTest.do_approx_equal_abs_test(n, 10)
        ApproxEqualInexactTest.do_approx_equal_abs_test(n, 2)

ApproxEqualInexactTest = test_statistics.ApproxEqualInexactTest()
test_approx_equal_absolute_ints()
