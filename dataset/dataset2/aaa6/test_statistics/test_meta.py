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

def test_meta():
    for meta in GlobalsTest.expected_metadata:
        GlobalsTest.assertTrue(hasattr(GlobalsTest.module, meta), '%s not present' % meta)

GlobalsTest = test_statistics.GlobalsTest()
test_meta()
