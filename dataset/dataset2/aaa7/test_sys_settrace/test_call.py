from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_call():
    RaisingTraceFuncTestCase.run_test_for_event('call')

RaisingTraceFuncTestCase = test_sys_settrace.RaisingTraceFuncTestCase()
test_call()
