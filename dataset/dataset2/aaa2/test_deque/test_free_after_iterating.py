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

def test_free_after_iterating():
    TestSequence.skipTest("Exhausted deque iterator doesn't free a deque")

TestSequence = test_deque.TestSequence()
test_free_after_iterating()
