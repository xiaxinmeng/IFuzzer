from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_03_one_instr():
    TraceTestCase.run_test(test_sys_settrace.one_instr_line)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_03_one_instr()
