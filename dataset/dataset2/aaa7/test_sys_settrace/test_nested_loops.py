from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_nested_loops():

    def func():
        for i in range(2):
            for j in range(2):
                a = i + j
        return a == 1
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (2, 'line'), (3, 'line'), (2, 'line'), (1, 'line'), (2, 'line'), (3, 'line'), (2, 'line'), (3, 'line'), (2, 'line'), (1, 'line'), (4, 'line'), (4, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_nested_loops()
