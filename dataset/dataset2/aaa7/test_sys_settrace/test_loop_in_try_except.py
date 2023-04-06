from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_loop_in_try_except():

    def func():
        try:
            for i in []:
                pass
            return 1
        except:
            return 2
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (3, 'line'), (3, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_loop_in_try_except()
