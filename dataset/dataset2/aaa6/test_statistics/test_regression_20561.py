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

def test_regression_20561():
    d = Decimal('1e4')
    TestMean.assertEqual(statistics.mean([d]), d)

TestMean = test_statistics.TestMean()
test_regression_20561()
