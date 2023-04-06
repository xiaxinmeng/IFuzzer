from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_21_repeated_pass():

    def func():
        pass
        pass
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line'), (2, 'line'), (2, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_21_repeated_pass()
