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

def test_repeat():
    TestBasicOps.assertEqual(operator.length_hint(repeat(None, 50)), 50)
    TestBasicOps.assertEqual(operator.length_hint(repeat(None, 0)), 0)
    TestBasicOps.assertEqual(operator.length_hint(repeat(None), 12), 12)

TestBasicOps = test_itertools.TestBasicOps()
test_repeat()
