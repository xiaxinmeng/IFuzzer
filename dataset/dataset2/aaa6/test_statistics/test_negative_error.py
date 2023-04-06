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

def test_negative_error():
    exc = statistics.StatisticsError
    for values in ([-1], [1, -2, 3]):
        with TestHarmonicMean.subTest(values=values):
            TestHarmonicMean.assertRaises(exc, TestHarmonicMean.func, values)

TestHarmonicMean = test_statistics.TestHarmonicMean()
TestHarmonicMean.setUp()
test_negative_error()
