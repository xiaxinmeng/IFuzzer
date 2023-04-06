from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(5, 8, [1, 3, 8, 10, 11, 13])
def test_jump_over_break_in_try_finally_block(output):
    output.append(1)
    while True:
        output.append(3)
        try:
            output.append(5)
            if not output:
                break
            output.append(8)
        finally:
            output.append(10)
        output.append(11)
        break
    output.append(13)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_over_break_in_try_finally_block()
