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

def test_instantiation_and_attributes():
    nd = TestNormalDist.module.NormalDist(500, 17)
    TestNormalDist.assertEqual(nd.mean, 500)
    TestNormalDist.assertEqual(nd.stdev, 17)
    TestNormalDist.assertEqual(nd.variance, 17 ** 2)
    nd = TestNormalDist.module.NormalDist()
    TestNormalDist.assertEqual(nd.mean, 0)
    TestNormalDist.assertEqual(nd.stdev, 1)
    TestNormalDist.assertEqual(nd.variance, 1 ** 2)
    with TestNormalDist.assertRaises(TestNormalDist.module.StatisticsError):
        TestNormalDist.module.NormalDist(500, -10)

    class NewNormalDist(TestNormalDist.module.NormalDist):
        pass
    nnd = NewNormalDist(200, 5)
    TestNormalDist.assertEqual(type(nnd), NewNormalDist)

TestNormalDist = test_statistics.TestNormalDist()
test_instantiation_and_attributes()
