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

def test_bad_tol():
    TestApproxEqualErrors.assertRaises(ValueError, test_statistics.approx_equal, 100, 100, -1, 0.1)

TestApproxEqualErrors = test_statistics.TestApproxEqualErrors()
test_bad_tol()
