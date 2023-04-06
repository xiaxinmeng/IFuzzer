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

def test_exactly_equal_decimals():
    D = Decimal
    for d in map(D, '8.2 31.274 912.04 16.745 1.2047'.split()):
        ApproxEqualExactTest.do_exactly_equal_test(d, 0, 0)

ApproxEqualExactTest = test_statistics.ApproxEqualExactTest()
test_exactly_equal_decimals()
