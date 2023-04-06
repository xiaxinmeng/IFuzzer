from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_10_ireturn():
    TraceTestCase.run_test(test_sys_settrace.ireturn_example)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_10_ireturn()
