from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_18_except_with_name():

    def func():
        try:
            try:
                raise Exception
            except Exception as e:
                raise
                x = 'Something'
                y = 'Something'
        except Exception:
            pass
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (3, 'exception'), (4, 'line'), (5, 'line'), (8, 'line'), (9, 'line'), (9, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_18_except_with_name()
