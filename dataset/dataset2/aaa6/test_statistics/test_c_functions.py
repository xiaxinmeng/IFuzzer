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

@unittest.skipUnless(test_statistics.c_statistics, 'requires _statistics')
def test_c_functions():
    for fname in TestModules.func_names:
        TestModules.assertEqual(getattr(test_statistics.c_statistics, fname).__module__, '_statistics')

TestModules = test_statistics.TestModules()
test_c_functions()
