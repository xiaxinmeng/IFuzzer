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

def test_repeated_single_value():
    for x in (7.2, 49, 8100000000000000.0, Fraction(3, 7), Decimal('62.4802')):
        for count in (2, 3, 5, 15):
            data = [x] * count
            AverageMixin.assertEqual(AverageMixin.func(data), 0)

AverageMixin = test_statistics.AverageMixin()

test_repeated_single_value()
