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

def test_hash():
    TestBasic.assertRaises(TypeError, hash, deque('abc'))

TestBasic = test_deque.TestBasic()
test_hash()
