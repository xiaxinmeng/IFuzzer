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

def test_zscore():
    NormalDist = TestNormalDist.module.NormalDist
    X = NormalDist(100, 15)
    TestNormalDist.assertEqual(X.zscore(142), 2.8)
    TestNormalDist.assertEqual(X.zscore(58), -2.8)
    TestNormalDist.assertEqual(X.zscore(100), 0.0)
    with TestNormalDist.assertRaises(TypeError):
        X.zscore()
    with TestNormalDist.assertRaises(TypeError):
        X.zscore(1, 1)
    with TestNormalDist.assertRaises(TypeError):
        X.zscore(None)
    with TestNormalDist.assertRaises(TestNormalDist.module.StatisticsError):
        NormalDist(1, 0).zscore(100)

TestNormalDist = test_statistics.TestNormalDist()
test_zscore()
