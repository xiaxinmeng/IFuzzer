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

def test_none_data():
    TestMode.assertRaises(TypeError, TestMode.func, None)

TestMode = test_statistics.TestMode()
TestMode.setUp()
test_none_data()
