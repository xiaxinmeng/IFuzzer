from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_08_settrace_and_return():
    TraceTestCase.run_test2(test_sys_settrace.settrace_and_return)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_08_settrace_and_return()
