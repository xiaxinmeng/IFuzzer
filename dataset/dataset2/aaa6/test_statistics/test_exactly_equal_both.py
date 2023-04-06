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

def test_exactly_equal_both():
    for x in [41017, 16.742, -813.02, Fraction(3, 8)]:
        ApproxEqualExactTest.do_exactly_equal_test(x, 0.1, 0.01)
    D = Decimal
    ApproxEqualExactTest.do_exactly_equal_test(D('7.2'), D('0.1'), D('0.01'))

ApproxEqualExactTest = test_statistics.ApproxEqualExactTest()
test_exactly_equal_both()
