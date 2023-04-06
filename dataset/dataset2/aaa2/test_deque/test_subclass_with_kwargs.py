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

def test_subclass_with_kwargs():
    test_deque.SubclassWithKwargs(newarg=1)

TestSubclassWithKwargs = test_deque.TestSubclassWithKwargs()
test_subclass_with_kwargs()
