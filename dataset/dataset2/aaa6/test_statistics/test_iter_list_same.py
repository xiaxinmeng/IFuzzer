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

def test_iter_list_same():
    data = [random.uniform(-3, 8) for _ in range(1000)]
    expected = VarianceStdevMixin.func(data)
    VarianceStdevMixin.assertEqual(VarianceStdevMixin.func(iter(data)), expected)

VarianceStdevMixin = test_statistics.VarianceStdevMixin()
test_iter_list_same()
