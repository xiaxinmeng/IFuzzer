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

def test_with_weights():
    TestHarmonicMean.assertEqual(TestHarmonicMean.func([40, 60], [5, 30]), 56.0)
    TestHarmonicMean.assertEqual(TestHarmonicMean.func([40, 60], weights=[5, 30]), 56.0)
    TestHarmonicMean.assertEqual(TestHarmonicMean.func(iter([40, 60]), iter([5, 30])), 56.0)
    TestHarmonicMean.assertEqual(TestHarmonicMean.func([Fraction(10, 3), Fraction(23, 5), Fraction(7, 2)], [5, 2, 10]), TestHarmonicMean.func([Fraction(10, 3)] * 5 + [Fraction(23, 5)] * 2 + [Fraction(7, 2)] * 10))
    TestHarmonicMean.assertEqual(TestHarmonicMean.func([10], [7]), 10)
    with TestHarmonicMean.assertRaises(TypeError):
        TestHarmonicMean.func([1, 2, 3], [1, (), 3])
    with TestHarmonicMean.assertRaises(statistics.StatisticsError):
        TestHarmonicMean.func([1, 2, 3], [1, 2])
    with TestHarmonicMean.assertRaises(statistics.StatisticsError):
        TestHarmonicMean.func([10], [0])
    with TestHarmonicMean.assertRaises(statistics.StatisticsError):
        TestHarmonicMean.func([10, 20], [0, 0])

TestHarmonicMean = test_statistics.TestHarmonicMean()
TestHarmonicMean.setUp()
test_with_weights()
