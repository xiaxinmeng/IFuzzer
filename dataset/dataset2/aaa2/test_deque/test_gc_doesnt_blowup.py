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

def test_gc_doesnt_blowup():
    import gc
    d = deque()
    for i in range(100):
        d.append(1)
        gc.collect()

TestBasic = test_deque.TestBasic()
test_gc_doesnt_blowup()
