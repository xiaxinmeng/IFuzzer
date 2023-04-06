from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_large_function():
    d = {}
    exec("def f(output):        # line 0\n            x = 0                     # line 1\n            y = 1                     # line 2\n            '''                       # line 3\n            %s                        # lines 4-1004\n            '''                       # line 1005\n            x += 1                    # line 1006\n            output.append(x)          # line 1007\n            return" % ('\n' * 1000,), d)
    f = d['f']
    JumpTestCase.run_test(f, 2, 1007, [0])

JumpTestCase = test_sys_settrace.JumpTestCase()
test_large_function()
