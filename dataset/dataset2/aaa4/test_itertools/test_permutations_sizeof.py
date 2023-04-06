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

def test_permutations_sizeof():
    basesize = support.calcobjsize('4Pni')
    check = SizeofTest.check_sizeof
    check(permutations('abcd'), basesize + 4 * SizeofTest.ssize_t + 4 * SizeofTest.ssize_t)
    check(permutations('abcd', 3), basesize + 4 * SizeofTest.ssize_t + 3 * SizeofTest.ssize_t)
    check(permutations('abcde', 3), basesize + 5 * SizeofTest.ssize_t + 3 * SizeofTest.ssize_t)
    check(permutations(range(10), 4), basesize + 10 * SizeofTest.ssize_t + 4 * SizeofTest.ssize_t)

SizeofTest = test_itertools.SizeofTest()
SizeofTest.setUp()
test_permutations_sizeof()
