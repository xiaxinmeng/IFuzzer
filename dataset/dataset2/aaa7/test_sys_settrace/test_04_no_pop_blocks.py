from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_04_no_pop_blocks():
    TraceTestCase.run_test(test_sys_settrace.no_pop_blocks)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_04_no_pop_blocks()
