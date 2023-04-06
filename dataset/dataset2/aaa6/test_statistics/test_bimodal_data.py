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

def test_bimodal_data():
    data = [1, 1, 2, 2, 2, 2, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9]
    assert data.count(2) == data.count(6) == 4
    TestMode.assertEqual(TestMode.func(data), 2)

TestMode = test_statistics.TestMode()
TestMode.setUp()
test_bimodal_data()
