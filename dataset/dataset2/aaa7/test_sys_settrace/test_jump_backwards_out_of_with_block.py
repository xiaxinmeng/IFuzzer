from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 1, [1, 2, 1, 2, 3, -2])
def test_jump_backwards_out_of_with_block(output):
    output.append(1)
    with tracecontext(output, 2):
        output.append(3)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_backwards_out_of_with_block()
