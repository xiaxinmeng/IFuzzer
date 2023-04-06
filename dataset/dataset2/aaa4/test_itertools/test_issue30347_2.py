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

def test_issue30347_2():

    class K:

        def __init__(RegressionTests, v):
            pass

        def __eq__(RegressionTests, other):
            nonlocal i
            i += 1
            if i == 1:
                next(g, None)
            return True
    i = 0
    g = next(groupby(range(10), K))[1]
    for j in range(2):
        next(g, None)

RegressionTests = test_itertools.RegressionTests()
test_issue30347_2()
