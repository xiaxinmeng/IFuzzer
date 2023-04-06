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

def test_stapmap():
    TestExamples.assertEqual(list(starmap(pow, [(2, 5), (3, 2), (10, 3)])), [32, 9, 1000])

TestExamples = test_itertools.TestExamples()
test_stapmap()
