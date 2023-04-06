from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_07_raise():
    TraceTestCase.run_test(test_sys_settrace.test_raise)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_07_raise()
