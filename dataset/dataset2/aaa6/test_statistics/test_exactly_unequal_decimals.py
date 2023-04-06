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

def test_exactly_unequal_decimals():
    for d in map(Decimal, '3.1415 298.12 3.47 18.996 0.00245'.split()):
        ApproxEqualUnequalTest.do_exactly_unequal_test(d)

ApproxEqualUnequalTest = test_statistics.ApproxEqualUnequalTest()
test_exactly_unequal_decimals()
