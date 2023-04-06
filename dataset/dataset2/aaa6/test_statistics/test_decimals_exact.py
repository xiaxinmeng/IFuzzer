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

def test_decimals_exact():
    D = Decimal
    TestHarmonicMean.assertEqual(TestHarmonicMean.func([D(15), D(30), D(60), D(60)]), D(30))
    data = [D('0.05'), D('0.10'), D('0.20'), D('0.20')]
    random.shuffle(data)
    TestHarmonicMean.assertEqual(TestHarmonicMean.func(data), D('0.10'))
    data = [D('1.68'), D('0.32'), D('5.94'), D('2.75')]
    random.shuffle(data)
    TestHarmonicMean.assertEqual(TestHarmonicMean.func(data), D(66528) / 70723)

TestHarmonicMean = test_statistics.TestHarmonicMean()
TestHarmonicMean.setUp()
test_decimals_exact()
