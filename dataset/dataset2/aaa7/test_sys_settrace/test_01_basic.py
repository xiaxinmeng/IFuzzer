from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_01_basic():
    TraceTestCase.run_test(test_sys_settrace.basic)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_01_basic()
