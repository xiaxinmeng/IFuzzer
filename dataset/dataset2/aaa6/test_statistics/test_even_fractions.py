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

def test_even_fractions():
    F = Fraction
    data = [F(5, 4), F(9, 4), F(13, 4), F(13, 4), F(17, 4), F(17, 4)]
    assert len(data) % 2 == 0
    random.shuffle(data)
    TestMedian.assertEqual(TestMedian.func(data), 3.25)

TestMedian = test_statistics.TestMedian()
TestMedian.setUp()
test_even_fractions()
