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

def test_odd_number_repeated():
    data = [12, 13, 14, 14, 14, 15, 15]
    assert len(data) % 2 == 1
    TestMedianGrouped.assertEqual(TestMedianGrouped.func(data), 14)
    data = [12, 13, 14, 14, 14, 14, 15]
    assert len(data) % 2 == 1
    TestMedianGrouped.assertEqual(TestMedianGrouped.func(data), 13.875)
    data = [5, 10, 10, 15, 20, 20, 20, 20, 25, 25, 30]
    assert len(data) % 2 == 1
    TestMedianGrouped.assertEqual(TestMedianGrouped.func(data, 5), 19.375)
    data = [16, 18, 18, 18, 18, 20, 20, 20, 22, 22, 22, 24, 24, 26, 28]
    assert len(data) % 2 == 1
    TestMedianGrouped.assertApproxEqual(TestMedianGrouped.func(data, 2), 20.66666667, tol=1e-08)

TestMedianGrouped = test_statistics.TestMedianGrouped()
TestMedianGrouped.setUp()
test_odd_number_repeated()
