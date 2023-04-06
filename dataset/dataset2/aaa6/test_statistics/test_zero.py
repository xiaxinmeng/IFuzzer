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

def test_zero():
    values = [1, 0, 2]
    TestHarmonicMean.assertEqual(TestHarmonicMean.func(values), 0)

TestHarmonicMean = test_statistics.TestHarmonicMean()
TestHarmonicMean.setUp()
test_zero()
