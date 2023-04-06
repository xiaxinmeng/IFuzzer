from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_15_loops():

    def for_example():
        for x in range(2):
            pass
    TraceTestCase.run_and_compare(for_example, [(0, 'call'), (1, 'line'), (2, 'line'), (1, 'line'), (2, 'line'), (1, 'line'), (1, 'return')])

    def while_example():
        x = 2
        while x > 0:
            x -= 1
    TraceTestCase.run_and_compare(while_example, [(0, 'call'), (2, 'line'), (3, 'line'), (4, 'line'), (3, 'line'), (4, 'line'), (3, 'line'), (3, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_15_loops()
