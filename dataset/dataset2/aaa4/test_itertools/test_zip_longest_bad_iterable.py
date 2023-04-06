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

def test_zip_longest_bad_iterable():
    exception = TypeError()

    class BadIterable:

        def __iter__(TestBasicOps):
            raise exception
    with TestBasicOps.assertRaises(TypeError) as cm:
        zip_longest(BadIterable())
    TestBasicOps.assertIs(cm.exception, exception)

TestBasicOps = test_itertools.TestBasicOps()
test_zip_longest_bad_iterable()
