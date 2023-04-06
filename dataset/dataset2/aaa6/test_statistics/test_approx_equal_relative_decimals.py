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

def test_approx_equal_relative_decimals():
    for d in map(Decimal, '0.02 1.0 5.7 13.67 94.138 91027.9321'.split()):
        ApproxEqualInexactTest.do_approx_equal_rel_test(d, Decimal('0.001'))
        ApproxEqualInexactTest.do_approx_equal_rel_test(-d, Decimal('0.05'))

ApproxEqualInexactTest = test_statistics.ApproxEqualInexactTest()
test_approx_equal_relative_decimals()
