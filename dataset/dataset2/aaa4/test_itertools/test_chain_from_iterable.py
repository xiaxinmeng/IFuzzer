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

def test_chain_from_iterable():
    a = []
    TestBasicOps.makecycle(chain.from_iterable([a]), a)

TestBasicOps = test_itertools.TestBasicOps()
TestBasicOps.setUp()
test_chain_from_iterable()
