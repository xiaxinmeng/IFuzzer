from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_line():
    RaisingTraceFuncTestCase.run_test_for_event('line')

RaisingTraceFuncTestCase = test_sys_settrace.RaisingTraceFuncTestCase()
test_line()
