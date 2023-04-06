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

def test_discrete_data():
    data = list(range(10))
    for i in range(10):
        d = data + [i]
        random.shuffle(d)
        TestMode.assertEqual(TestMode.func(d), i)

TestMode = test_statistics.TestMode()
TestMode.setUp()
test_discrete_data()
