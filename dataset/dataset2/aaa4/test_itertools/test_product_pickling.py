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

def test_product_pickling():
    for (args, result) in [([], [()]), (['ab'], [('a',), ('b',)]), ([range(2), range(3)], [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]), ([range(0), range(2), range(3)], []), ([range(2), range(0), range(3)], []), ([range(2), range(3), range(0)], [])]:
        TestBasicOps.assertEqual(list(copy.copy(product(*args))), result)
        TestBasicOps.assertEqual(list(copy.deepcopy(product(*args))), result)
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            TestBasicOps.pickletest(proto, product(*args))

TestBasicOps = test_itertools.TestBasicOps()
test_product_pickling()
