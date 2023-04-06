import unittest
from test import support
from itertools import *
import weakref
from decimal import Decimal
from fractions import Fraction
import operator
import random
import copy
import pickle
from functools import reduce
import sys
import struct
import threading
import gc
import gc
import test_itertools

def test_repeat_with_negative_times():
    TestBasicOps.assertEqual(operator.length_hint(repeat(None, -1)), 0)
    TestBasicOps.assertEqual(operator.length_hint(repeat(None, -2)), 0)
    TestBasicOps.assertEqual(operator.length_hint(repeat(None, times=-1)), 0)
    TestBasicOps.assertEqual(operator.length_hint(repeat(None, times=-2)), 0)

TestBasicOps = test_itertools.TestBasicOps()
test_repeat_with_negative_times()
