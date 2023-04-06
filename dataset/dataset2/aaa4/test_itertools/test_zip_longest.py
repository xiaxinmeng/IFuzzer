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

def test_zip_longest():
    a = []
    TestExamples.makecycle(zip_longest([a] * 2, [a] * 3), a)
    b = [a, None]
    TestExamples.makecycle(zip_longest([a] * 2, [a] * 3, fillvalue=b), a)

TestExamples = test_itertools.TestExamples()
test_zip_longest()
