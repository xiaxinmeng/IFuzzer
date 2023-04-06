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

def test_float_inf():
    inf = float('inf')
    for sign in (+1, -1):
        SumSpecialValues.do_test_inf(sign * inf)

SumSpecialValues = test_statistics.SumSpecialValues()
test_float_inf()
