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

@support.impl_detail('tuple reuse is specific to CPython')
def test_combinations_tuple_reuse():
    TestBasicOps.assertEqual(len(set(map(id, combinations('abcde', 3)))), 1)
    TestBasicOps.assertNotEqual(len(set(map(id, list(combinations('abcde', 3))))), 1)

TestBasicOps = test_itertools.TestBasicOps()
test_combinations_tuple_reuse()
