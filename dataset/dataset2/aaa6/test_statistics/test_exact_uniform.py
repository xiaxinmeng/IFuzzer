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

def test_exact_uniform():
    data = list(range(10000))
    random.shuffle(data)
    expected = (10000 ** 2 - 1) / 12
    TestPVariance.assertEqual(TestPVariance.func(data), expected)

TestPVariance = test_statistics.TestPVariance()
TestPVariance.setUp()
test_exact_uniform()
