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

def test_py_functions():
    for fname in TestModules.func_names:
        TestModules.assertEqual(getattr(test_statistics.py_statistics, fname).__module__, 'statistics')

TestModules = test_statistics.TestModules()
test_py_functions()
