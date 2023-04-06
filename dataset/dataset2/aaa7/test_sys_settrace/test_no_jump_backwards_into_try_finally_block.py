from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(5, 2, [2, 4], (ValueError, 'into'))
def test_no_jump_backwards_into_try_finally_block(output):
    try:
        output.append(2)
    finally:
        output.append(4)
    output.append(5)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_backwards_into_try_finally_block()
