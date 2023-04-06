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
def test_combinations_with_replacement_tuple_reuse():
    cwr = combinations_with_replacement
    TestBasicOps.assertEqual(len(set(map(id, cwr('abcde', 3)))), 1)
    TestBasicOps.assertNotEqual(len(set(map(id, list(cwr('abcde', 3))))), 1)

TestBasicOps = test_itertools.TestBasicOps()
test_combinations_with_replacement_tuple_reuse()
