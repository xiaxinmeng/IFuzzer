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

def test_tee_del_backward():
    (forward, backward) = tee(repeat(None, 20000000))
    try:
        any(forward)
        del backward
    except:
        del forward, backward
        raise

TestBasicOps = test_itertools.TestBasicOps()
test_tee_del_backward()
