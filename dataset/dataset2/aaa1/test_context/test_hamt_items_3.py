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

def test_hamt_items_3():
    h = hamt()
    HamtTest.assertEqual(len(h.items()), 0)
    HamtTest.assertEqual(list(h.items()), [])

HamtTest = test_context.HamtTest()
test_hamt_items_3()
