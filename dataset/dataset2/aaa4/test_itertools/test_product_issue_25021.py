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

def test_product_issue_25021():
    p = product((1, 2), (3,))
    p.__setstate__((0, 4096))
    TestBasicOps.assertEqual(next(p), (2, 3))
    p = product((1, 2), (), (3,))
    p.__setstate__((0, 0, 4096))
    TestBasicOps.assertRaises(StopIteration, next, p)

TestBasicOps = test_itertools.TestBasicOps()
test_product_issue_25021()
