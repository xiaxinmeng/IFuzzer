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

def test_exactly_equal_fractions():
    F = Fraction
    for f in [F(1, 2), F(0), F(5, 3), F(9, 7), F(35, 36), F(3, 7)]:
        ApproxEqualExactTest.do_exactly_equal_test(f, 0, 0)

ApproxEqualExactTest = test_statistics.ApproxEqualExactTest()
test_exactly_equal_fractions()
