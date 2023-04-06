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
def test_product_tuple_reuse():
    TestBasicOps.assertEqual(len(set(map(id, product('abc', 'def')))), 1)
    TestBasicOps.assertNotEqual(len(set(map(id, list(product('abc', 'def'))))), 1)

TestBasicOps = test_itertools.TestBasicOps()
test_product_tuple_reuse()
