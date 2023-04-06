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

def test_doubled_data():
    data = [random.uniform(1, 5) for _ in range(1000)]
    expected = TestMean.func(data)
    actual = TestMean.func(data * 2)
    TestMean.assertApproxEqual(actual, expected)

TestMean = test_statistics.TestMean()
TestMean.setUp()
test_doubled_data()
