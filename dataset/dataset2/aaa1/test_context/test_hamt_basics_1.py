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

def test_hamt_basics_1():
    h = hamt()
    h = None

HamtTest = test_context.HamtTest()
test_hamt_basics_1()
