from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_19_except_with_finally():

    def func():
        try:
            try:
                raise Exception
            finally:
                y = 'Something'
        except Exception:
            b = 23
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (3, 'exception'), (5, 'line'), (6, 'line'), (7, 'line'), (7, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_19_except_with_finally()
