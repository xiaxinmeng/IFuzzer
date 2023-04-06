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

def test_floats_exact():
    data = [1 / 8, 1 / 4, 1 / 4, 1 / 2, 1 / 2]
    random.shuffle(data)
    TestHarmonicMean.assertEqual(TestHarmonicMean.func(data), 1 / 4)
    TestHarmonicMean.assertEqual(TestHarmonicMean.func([0.25, 0.5, 1.0, 1.0]), 0.5)

TestHarmonicMean = test_statistics.TestHarmonicMean()
TestHarmonicMean.setUp()
test_floats_exact()
