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

def test_mismatched_infs():
    data = [2, 4, 6, float('inf'), 1, 3, 5, float('-inf')]
    result = TestMean.func(data)
    TestMean.assertTrue(math.isnan(result))

TestMean = test_statistics.TestMean()
TestMean.setUp()
test_mismatched_infs()
