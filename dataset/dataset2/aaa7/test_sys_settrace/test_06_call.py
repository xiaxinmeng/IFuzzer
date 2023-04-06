from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_06_call():
    TraceTestCase.run_test(test_sys_settrace.call)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_06_call()
