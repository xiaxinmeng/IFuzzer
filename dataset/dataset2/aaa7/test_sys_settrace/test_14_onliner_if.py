from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_14_onliner_if():

    def onliners():
        if True:
            x = False
        else:
            x = True
        return 0
    TraceTestCase.run_and_compare(onliners, [(0, 'call'), (1, 'line'), (3, 'line'), (3, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_14_onliner_if()
