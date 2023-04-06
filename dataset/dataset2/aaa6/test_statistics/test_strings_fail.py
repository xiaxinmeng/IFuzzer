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

def test_strings_fail():
    TestSum.assertRaises(TypeError, TestSum.func, [1, 2, 3], '999')
    TestSum.assertRaises(TypeError, TestSum.func, [1, 2, 3, '999'])

TestSum = test_statistics.TestSum()
TestSum.setUp()
test_strings_fail()
