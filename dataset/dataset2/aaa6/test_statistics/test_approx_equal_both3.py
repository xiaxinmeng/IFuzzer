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

def test_approx_equal_both3():
    ApproxEqualInexactTest.do_check_both(7.955, 7.952, 0.001, 0.00038, False, True)

ApproxEqualInexactTest = test_statistics.ApproxEqualInexactTest()
test_approx_equal_both3()
