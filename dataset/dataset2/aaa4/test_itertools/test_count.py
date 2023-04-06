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

def test_count():
    a = []
    Int = type('Int', (int,), dict(x=a))
    TestBasicOps.makecycle(count(Int(0), Int(1)), a)

TestBasicOps = test_itertools.TestBasicOps()
test_count()
