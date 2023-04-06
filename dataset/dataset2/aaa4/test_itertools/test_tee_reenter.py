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

def test_tee_reenter():

    class I:
        first = True

        def __iter__(TestBasicOps):
            return TestBasicOps

        def __next__(TestBasicOps):
            first = TestBasicOps.first
            TestBasicOps.first = False
            if first:
                return next(b)
    (a, b) = tee(I())
    with TestBasicOps.assertRaisesRegex(RuntimeError, 'tee'):
        next(a)

TestBasicOps = test_itertools.TestBasicOps()
test_tee_reenter()
