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

def test_odd_decimals():
    D = Decimal
    data = [D('5.5'), D('6.5'), D('6.5'), D('7.5'), D('8.5')]
    assert len(data) % 2 == 1
    random.shuffle(data)
    TestMedian.assertEqual(TestMedian.func(data), 6.75)

TestMedian = test_statistics.TestMedian()
TestMedian.setUp()
test_odd_decimals()
