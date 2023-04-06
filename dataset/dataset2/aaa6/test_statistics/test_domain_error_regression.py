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

def test_domain_error_regression():
    data = [0.123456789012345] * 10000
    result = VarianceStdevMixin.func(data)
    VarianceStdevMixin.assertApproxEqual(result, 0.0, tol=5e-17)
    VarianceStdevMixin.assertGreaterEqual(result, 0)

VarianceStdevMixin = test_statistics.VarianceStdevMixin()

test_domain_error_regression()
