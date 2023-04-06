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

def test_exactly_equal_floats():
    for x in [0.42, 1.974, 1497.4, 23.0, 179.5, 70.0245, 36.587]:
        ApproxEqualExactTest.do_exactly_equal_test(x, 0, 0)

ApproxEqualExactTest = test_statistics.ApproxEqualExactTest()
test_exactly_equal_floats()
