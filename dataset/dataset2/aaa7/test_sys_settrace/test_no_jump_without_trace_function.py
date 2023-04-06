from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

def test_no_jump_without_trace_function():
    test_sys_settrace.no_jump_without_trace_function()

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_without_trace_function()
