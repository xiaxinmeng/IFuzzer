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

def test_odd_ints():
    data = [1, 2, 3, 4, 5, 6, 9]
    assert len(data) % 2 == 1
    TestMedian.assertEqual(TestMedian.func(data), 4)

TestMedian = test_statistics.TestMedian()
TestMedian.setUp()
test_odd_ints()
