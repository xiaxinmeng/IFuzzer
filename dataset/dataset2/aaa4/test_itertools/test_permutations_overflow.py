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

@support.bigaddrspacetest
def test_permutations_overflow():
    with TestBasicOps.assertRaises((OverflowError, MemoryError)):
        permutations('A', 2 ** 30)

TestBasicOps = test_itertools.TestBasicOps()
test_permutations_overflow()
