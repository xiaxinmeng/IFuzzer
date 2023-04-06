from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_break_to_continue2():

    def func():
        TRUE = 1
        x = [1]
        while x:
            x.pop()
            while TRUE:
                break
            else:
                continue
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (4, 'line'), (5, 'line'), (6, 'line'), (3, 'line'), (3, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_break_to_continue2()
