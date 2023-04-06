from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 6, [2, 6, 7])
def test_jump_into_finally_block_from_try_block(output):
    try:
        output.append(2)
        output.append(3)
    finally:
        output.append(5)
        output.append(6)
    output.append(7)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_into_finally_block_from_try_block()
