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

def test_product_sizeof():
    basesize = support.calcobjsize('3Pi')
    check = SizeofTest.check_sizeof
    check(product('ab', '12'), basesize + 2 * SizeofTest.ssize_t)
    check(product(*('abc',) * 10), basesize + 10 * SizeofTest.ssize_t)

SizeofTest = test_itertools.SizeofTest()
SizeofTest.setUp()
test_product_sizeof()
