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

def test_error_msg():
    msg = 'badness #%d' % random.randint(10000, 99999)
    try:
        next(statistics._fail_neg([-1], msg))
    except statistics.StatisticsError as e:
        errmsg = e.args[0]
    else:
        FailNegTest.fail("expected exception, but it didn't happen")
    FailNegTest.assertEqual(errmsg, msg)

FailNegTest = test_statistics.FailNegTest()
test_error_msg()
