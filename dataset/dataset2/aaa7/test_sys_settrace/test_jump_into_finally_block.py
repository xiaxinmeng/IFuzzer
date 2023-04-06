from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(1, 5, [5])
def test_jump_into_finally_block(output):
    output.append(1)
    try:
        output.append(3)
    finally:
        output.append(5)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_into_finally_block()
