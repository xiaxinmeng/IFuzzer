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

def test_check_all():
    module = GlobalsTest.module
    for name in module.__all__:
        GlobalsTest.assertFalse(name.startswith('_'), 'private name "%s" in __all__' % name)
        GlobalsTest.assertTrue(hasattr(module, name), 'missing name "%s" in __all__' % name)

GlobalsTest = test_statistics.GlobalsTest()
test_check_all()
