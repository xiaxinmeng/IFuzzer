from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_12_tighterloop():
    TraceTestCase.run_test(test_sys_settrace.tighterloop_example)

TraceTestCase = test_sys_settrace.TraceTestCase()
test_12_tighterloop()
