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

def test_error_msg_numeric():
    args = (2.5, 4.0, 0.5, 0.25, None)
    TestNumericTestCase.do_test(args)

TestNumericTestCase = test_statistics.TestNumericTestCase()
test_error_msg_numeric()
