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

def test_compare_with_math_fsum():
    data = [random.uniform(-100, 1000) for _ in range(1000)]
    TestSum.assertApproxEqual(float(TestSum.func(data)[1]), math.fsum(data), rel=2e-16)

TestSum = test_statistics.TestSum()
TestSum.setUp()
test_compare_with_math_fsum()
