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

def test_exactly_unequal_ints():
    for n in [951, 572305, 478, 917, 17240]:
        ApproxEqualUnequalTest.do_exactly_unequal_test(n)

ApproxEqualUnequalTest = test_statistics.ApproxEqualUnequalTest()
test_exactly_unequal_ints()
