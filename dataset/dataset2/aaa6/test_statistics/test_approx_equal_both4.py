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

def test_approx_equal_both4():
    ApproxEqualInexactTest.do_check_both(2.78, 2.75, 0.01, 0.001, False, False)
    ApproxEqualInexactTest.do_check_both(971.44, 971.47, 0.02, 3e-05, False, False)

ApproxEqualInexactTest = test_statistics.ApproxEqualInexactTest()
test_approx_equal_both4()
