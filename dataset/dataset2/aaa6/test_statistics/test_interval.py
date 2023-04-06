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

def test_interval():
    data = [2.25, 2.5, 2.5, 2.75, 2.75, 3.0, 3.0, 3.25, 3.5, 3.75]
    TestMedianGrouped.assertEqual(TestMedianGrouped.func(data, 0.25), 2.875)
    data = [2.25, 2.5, 2.5, 2.75, 2.75, 2.75, 3.0, 3.0, 3.25, 3.5, 3.75]
    TestMedianGrouped.assertApproxEqual(TestMedianGrouped.func(data, 0.25), 2.83333333, tol=1e-08)
    data = [220, 220, 240, 260, 260, 260, 260, 280, 280, 300, 320, 340]
    TestMedianGrouped.assertEqual(TestMedianGrouped.func(data, 20), 265.0)

TestMedianGrouped = test_statistics.TestMedianGrouped()
TestMedianGrouped.setUp()
test_interval()
