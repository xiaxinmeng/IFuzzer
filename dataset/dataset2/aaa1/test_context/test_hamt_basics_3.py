import concurrent.futures
import contextvars
import functools
import gc
import random
import time
import unittest
import weakref
from _testcapi import hamt
import test_context

def test_hamt_basics_3():
    h = hamt()
    o = object()
    h1 = h.set('1', o)
    h2 = h1.set('1', o)
    HamtTest.assertIs(h1, h2)

HamtTest = test_context.HamtTest()
test_hamt_basics_3()
