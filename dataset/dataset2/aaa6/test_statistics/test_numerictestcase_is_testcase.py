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

def test_numerictestcase_is_testcase():
    TestNumericTestCase.assertTrue(issubclass(test_statistics.NumericTestCase, unittest.TestCase))

TestNumericTestCase = test_statistics.TestNumericTestCase()
test_numerictestcase_is_testcase()
