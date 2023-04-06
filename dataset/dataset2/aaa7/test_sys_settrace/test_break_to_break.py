from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_break_to_break():

    def func():
        TRUE = 1
        while TRUE:
            while TRUE:
                break
            break
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (4, 'line'), (5, 'line'), (5, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_break_to_break()
