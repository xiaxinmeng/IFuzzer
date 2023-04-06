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

def test_combinations_sizeof():
    basesize = support.calcobjsize('3Pni')
    check = SizeofTest.check_sizeof
    check(combinations('abcd', 3), basesize + 3 * SizeofTest.ssize_t)
    check(combinations(range(10), 4), basesize + 4 * SizeofTest.ssize_t)

SizeofTest = test_itertools.SizeofTest()
SizeofTest.setUp()
test_combinations_sizeof()
