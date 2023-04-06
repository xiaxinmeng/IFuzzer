from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(5, 11, [2, 4], (ValueError, 'after'))
def test_no_jump_over_return_try_finally_in_finally_block(output):
    try:
        output.append(2)
    finally:
        output.append(4)
        output.append(5)
        return
        try:
            output.append(8)
        finally:
            output.append(10)
        pass
    output.append(12)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_over_return_try_finally_in_finally_block()
