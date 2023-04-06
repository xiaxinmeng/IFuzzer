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

def test_hamt_basics_4():
    h = hamt()
    h1 = h.set('key', [])
    h2 = h1.set('key', [])
    HamtTest.assertIsNot(h1, h2)
    HamtTest.assertEqual(len(h1), 1)
    HamtTest.assertEqual(len(h2), 1)
    HamtTest.assertIsNot(h1.get('key'), h2.get('key'))

HamtTest = test_context.HamtTest()
test_hamt_basics_4()
