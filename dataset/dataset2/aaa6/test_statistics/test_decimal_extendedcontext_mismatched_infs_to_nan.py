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

def test_decimal_extendedcontext_mismatched_infs_to_nan():
    inf = Decimal('inf')
    data = [1, 2, inf, 3, -inf, 4]
    with decimal.localcontext(decimal.ExtendedContext):
        SumSpecialValues.assertTrue(math.isnan(statistics._sum(data)[1]))

SumSpecialValues = test_statistics.SumSpecialValues()
test_decimal_extendedcontext_mismatched_infs_to_nan()
