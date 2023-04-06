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

def test_compare_to_variance():
    data = [random.uniform(-2, 9) for _ in range(1000)]
    expected = math.sqrt(statistics.variance(data))
    TestPStdev.assertEqual(TestPStdev.func(data), expected)

TestPStdev = test_statistics.TestPStdev()
TestPStdev.setUp()
test_compare_to_variance()
