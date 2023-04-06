from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 5, [1, 2, 5, -2])
def test_jump_between_with_blocks(output):
    output.append(1)
    with tracecontext(output, 2):
        output.append(3)
    with tracecontext(output, 4):
        output.append(5)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_between_with_blocks()
