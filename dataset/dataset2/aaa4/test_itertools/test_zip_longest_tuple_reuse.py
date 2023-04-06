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
def test_zip_longest_tuple_reuse():
    ids = list(map(id, zip_longest('abc', 'def')))
    TestBasicOps.assertEqual(min(ids), max(ids))
    ids = list(map(id, list(zip_longest('abc', 'def'))))
    TestBasicOps.assertEqual(len(dict.fromkeys(ids)), len(ids))

TestBasicOps = test_itertools.TestBasicOps()
test_zip_longest_tuple_reuse()
