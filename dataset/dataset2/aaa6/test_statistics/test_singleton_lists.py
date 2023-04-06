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

def test_singleton_lists():
    for x in range(1, 101):
        TestHarmonicMean.assertEqual(TestHarmonicMean.func([x]), x)

TestHarmonicMean = test_statistics.TestHarmonicMean()
TestHarmonicMean.setUp()
test_singleton_lists()
