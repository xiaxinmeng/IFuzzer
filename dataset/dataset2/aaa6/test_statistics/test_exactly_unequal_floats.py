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

def test_exactly_unequal_floats():
    for x in [9.51, 5723.05, 47.8, 9.17, 17.24]:
        ApproxEqualUnequalTest.do_exactly_unequal_test(x)

ApproxEqualUnequalTest = test_statistics.ApproxEqualUnequalTest()
test_exactly_unequal_floats()
