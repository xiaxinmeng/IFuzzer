from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_17_none_f_trace():

    def func():
        sys._getframe().f_trace = None
        lineno = 2
    TraceTestCase.run_and_compare(func, [(0, 'call'), (1, 'line')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_17_none_f_trace()
