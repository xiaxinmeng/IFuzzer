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

def test_bad_arg_types():
    UnivariateCommonMixin.check_for_type_error(None)
    UnivariateCommonMixin.check_for_type_error(23)
    UnivariateCommonMixin.check_for_type_error(42.0)
    UnivariateCommonMixin.check_for_type_error(object())

UnivariateCommonMixin = test_statistics.UnivariateCommonMixin()

test_bad_arg_types()
