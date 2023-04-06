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

def test_properties():
    X = TestNormalDist.module.NormalDist(100, 15)
    TestNormalDist.assertEqual(X.mean, 100)
    TestNormalDist.assertEqual(X.median, 100)
    TestNormalDist.assertEqual(X.mode, 100)
    TestNormalDist.assertEqual(X.stdev, 15)
    TestNormalDist.assertEqual(X.variance, 225)

TestNormalDist = test_statistics.TestNormalDist()
test_properties()
