from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_11_tightloop():
    TraceTestCase.run_test(test_sys_settrace.tightloop_example)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_11_tightloop()
