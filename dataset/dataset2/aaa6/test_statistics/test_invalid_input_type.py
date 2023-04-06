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

def test_invalid_input_type():
    with ConvertTest.assertRaises(TypeError):
        statistics._convert(None, float)

ConvertTest = test_statistics.ConvertTest()
test_invalid_input_type()
