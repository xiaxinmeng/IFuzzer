from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_try_except_with_wrong_type():

    def func():
        try:
            2 / 0
        except IndexError:
            4
        finally:
            return 6
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (2, 'exception'), (3, 'line'), (6, 'line'), (6, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_try_except_with_wrong_type()
