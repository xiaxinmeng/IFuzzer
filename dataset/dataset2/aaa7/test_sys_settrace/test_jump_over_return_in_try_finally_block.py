from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 6, [1, 6, 8, 9])
def test_jump_over_return_in_try_finally_block(output):
    output.append(1)
    try:
        output.append(3)
        if not output:
            return
        output.append(6)
    finally:
        output.append(8)
    output.append(9)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_over_return_in_try_finally_block()
