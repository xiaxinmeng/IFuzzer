from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_set_and_retrieve_func():

    def fn(*args):
        pass
    sys.settrace(fn)
    try:
        assert sys.gettrace() is fn
    finally:
        sys.settrace(None)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_set_and_retrieve_func()
