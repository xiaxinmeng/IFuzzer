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

def test_decimal_snan_raises():
    sNAN = Decimal('sNAN')
    data = [1, sNAN, 2]
    SumSpecialValues.assertRaises(decimal.InvalidOperation, statistics._sum, data)

SumSpecialValues = test_statistics.SumSpecialValues()
test_decimal_snan_raises()
