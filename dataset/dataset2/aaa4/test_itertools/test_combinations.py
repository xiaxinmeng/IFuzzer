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

def test_combinations():
    a = []
    TestBasicOps.makecycle(combinations([1, 2, a, 3], 3), a)

TestBasicOps = test_itertools.TestBasicOps()
test_combinations()
