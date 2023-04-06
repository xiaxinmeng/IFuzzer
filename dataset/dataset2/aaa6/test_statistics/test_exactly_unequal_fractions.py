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

def test_exactly_unequal_fractions():
    F = Fraction
    for f in [F(1, 5), F(7, 9), F(12, 11), F(101, 99023)]:
        ApproxEqualUnequalTest.do_exactly_unequal_test(f)

ApproxEqualUnequalTest = test_statistics.ApproxEqualUnequalTest()
test_exactly_unequal_fractions()
