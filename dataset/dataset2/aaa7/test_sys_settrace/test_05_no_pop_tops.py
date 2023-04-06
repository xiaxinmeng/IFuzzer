from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_05_no_pop_tops():
    TraceTestCase.run_test(test_sys_settrace.no_pop_tops)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_05_no_pop_tops()
