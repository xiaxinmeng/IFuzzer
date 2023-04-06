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

def test_nominal_data():
    data = 'abcbdb'
    TestMode.assertEqual(TestMode.func(data), 'b')
    data = 'fe fi fo fum fi fi'.split()
    TestMode.assertEqual(TestMode.func(data), 'fi')

TestMode = test_statistics.TestMode()
TestMode.setUp()
test_nominal_data()
