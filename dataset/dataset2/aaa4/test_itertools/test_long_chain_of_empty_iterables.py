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

@support.skip_if_pgo_task
def test_long_chain_of_empty_iterables():
    it = chain.from_iterable((() for unused in range(10000000)))
    with RegressionTests.assertRaises(StopIteration):
        next(it)

RegressionTests = test_itertools.RegressionTests()
test_long_chain_of_empty_iterables()
