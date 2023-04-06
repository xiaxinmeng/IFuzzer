from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(2, 3, [1], event='call', error=(ValueError, "can't jump from the 'call' trace event of a new frame"))
def test_no_jump_from_call(output):
    output.append(1)

    def nested():
        output.append(3)
    nested()
    output.append(5)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_from_call()
