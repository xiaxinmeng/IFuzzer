from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_return_through_finally():

    def func():
        try:
            return 2
        finally:
            4
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (4, 'line'), (4, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_return_through_finally()
