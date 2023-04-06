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

def test_has_exception():
    errmsg = 'Expected StatisticsError to be a ValueError, but got a subclass of %r instead.'
    StatisticsErrorTest.assertTrue(hasattr(statistics, 'StatisticsError'))
    StatisticsErrorTest.assertTrue(issubclass(statistics.StatisticsError, ValueError), errmsg % statistics.StatisticsError.__base__)

StatisticsErrorTest = test_statistics.StatisticsErrorTest()
test_has_exception()
