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

def test_center_not_at_mean():
    data = (1.0, 2.0)
    TestVariance.assertEqual(TestVariance.func(data, xbar=2.0), 1.0)

TestVariance = test_statistics.TestVariance()
TestVariance.setUp()
test_center_not_at_mean()
