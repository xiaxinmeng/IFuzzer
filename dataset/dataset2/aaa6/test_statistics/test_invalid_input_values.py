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

def test_invalid_input_values():
    for (a, l, x) in [([1], 2, 1), ([1, 3], 0, 2)]:
        with FindLteqTest.assertRaises(ValueError):
            statistics._find_rteq(a, l, x)

FindLteqTest = test_statistics.FindLteqTest()
test_invalid_input_values()
