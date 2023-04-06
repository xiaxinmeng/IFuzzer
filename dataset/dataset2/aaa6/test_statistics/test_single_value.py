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

def test_single_value():
    for x in (81, 203.74, 390000000000000.0, Fraction(5, 21), Decimal('35.719')):
        AverageMixin.assertRaises(statistics.StatisticsError, AverageMixin.func, [x])

AverageMixin = test_statistics.AverageMixin()
test_single_value()
