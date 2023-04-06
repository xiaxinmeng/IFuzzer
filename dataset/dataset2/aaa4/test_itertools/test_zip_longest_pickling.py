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

def test_zip_longest_pickling():
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        TestBasicOps.pickletest(proto, zip_longest('abc', 'def'))
        TestBasicOps.pickletest(proto, zip_longest('abc', 'defgh'))
        TestBasicOps.pickletest(proto, zip_longest('abc', 'defgh', fillvalue=1))
        TestBasicOps.pickletest(proto, zip_longest('', 'defgh'))

TestBasicOps = test_itertools.TestBasicOps()
test_zip_longest_pickling()
