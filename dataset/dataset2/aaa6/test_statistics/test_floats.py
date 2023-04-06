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

def test_floats():
    data = [17.25, 19.75, 20.0, 21.5, 21.75, 23.25, 25.125, 27.5]
    random.shuffle(data)
    TestSum.assertEqual(TestSum.func(data), 22.015625)

TestSum = test_statistics.TestSum()
TestSum.setUp()
test_floats()
