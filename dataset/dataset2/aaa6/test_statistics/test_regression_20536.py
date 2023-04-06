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

def test_regression_20536():
    t = statistics._exact_ratio(Decimal('1e2'))
    DecimalToRatioTest.assertEqual(t, (100, 1))
    t = statistics._exact_ratio(Decimal('1.47e5'))
    DecimalToRatioTest.assertEqual(t, (147000, 1))

DecimalToRatioTest = test_statistics.DecimalToRatioTest()
test_regression_20536()
