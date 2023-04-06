from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_16_blank_lines():
    namespace = {}
    exec('def f():\n' + '\n' * 256 + '    pass', namespace)
    TraceTestCase.run_and_compare(namespace['f'], [(0, 'call'), (257, 'line'), (257, 'return')])

TraceTestCase = test_sys_settrace.TraceTestCase()
test_16_blank_lines()
