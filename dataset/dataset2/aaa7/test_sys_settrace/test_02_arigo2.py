from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_02_arigo2():
    TraceTestCase.run_test(test_sys_settrace.arigo_example2)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_02_arigo2()
