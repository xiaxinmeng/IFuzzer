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

@support.cpython_only
def test_zip_longest_result_gc():
    it = zip_longest([[]])
    gc.collect()
    TestBasicOps.assertTrue(gc.is_tracked(next(it)))

TestBasicOps = test_itertools.TestBasicOps()
test_zip_longest_result_gc()
