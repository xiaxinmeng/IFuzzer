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

def test_counter_data():
    data = collections.Counter([1, 1, 1, 2])
    TestMode.assertEqual(TestMode.func(data), 1)

TestMode = test_statistics.TestMode()
TestMode.setUp()
test_counter_data()
