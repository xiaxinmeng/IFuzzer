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

def test_ints():
    data = [4, 7, 13, 16]
    exact = 30
    TestSum.assertEqual(TestSum.func(data), exact)

TestSum = test_statistics.TestSum()
TestSum.setUp()
test_ints()
