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

def test_even_number_repeated():
    data = [5, 10, 10, 15, 20, 20, 20, 25, 25, 30]
    assert len(data) % 2 == 0
    TestMedianGrouped.assertApproxEqual(TestMedianGrouped.func(data, 5), 19.16666667, tol=1e-08)
    data = [2, 3, 4, 4, 4, 5]
    assert len(data) % 2 == 0
    TestMedianGrouped.assertApproxEqual(TestMedianGrouped.func(data), 3.83333333, tol=1e-08)
    data = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6]
    assert len(data) % 2 == 0
    TestMedianGrouped.assertEqual(TestMedianGrouped.func(data), 4.5)
    data = [3, 4, 4, 4, 5, 5, 5, 5, 6, 6]
    assert len(data) % 2 == 0
    TestMedianGrouped.assertEqual(TestMedianGrouped.func(data), 4.75)

TestMedianGrouped = test_statistics.TestMedianGrouped()
TestMedianGrouped.setUp()
test_even_number_repeated()
