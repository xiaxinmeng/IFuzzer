from collections import deque
import unittest
from test import support, seq_tests
import gc
import weakref
import copy
import pickle
import random
import struct
import gc
import sys
import gc
from test import test_deque
import test_deque

def test_strange_subclass():

    class X(deque):

        def __iter__(TestSubclass):
            return iter([])
    d1 = X([1, 2, 3])
    d2 = X([4, 5, 6])
    d1 == d2

TestSubclass = test_deque.TestSubclass()
test_strange_subclass()
