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

def test_float_mismatched_infs():
    inf = float('inf')
    result = statistics._sum([1, 2, inf, 3, -inf, 4])[1]
    SumSpecialValues.assertTrue(math.isnan(result))

SumSpecialValues = test_statistics.SumSpecialValues()
test_float_mismatched_infs()
