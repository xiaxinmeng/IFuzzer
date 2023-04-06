from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_if_break():

    def func():
        seq = [1, 0]
        while seq:
            n = seq.pop()
            if n:
                break
        else:
            n = 99
        return n
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (4, 'line'), (2, 'line'), (3, 'line'), (4, 'line'), (5, 'line'), (8, 'line'), (8, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_if_break()
