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

def test_exactly_equal_ints():
    for n in [42, 19740, 14974, 230, 1795, 700245, 36587]:
        ApproxEqualExactTest.do_exactly_equal_test(n, 0, 0)

ApproxEqualExactTest = test_statistics.ApproxEqualExactTest()
test_exactly_equal_ints()
