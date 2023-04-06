from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(6, 7, [2, 7], (ZeroDivisionError, ''))
def test_jump_in_nested_finally_2(output):
    try:
        output.append(2)
        1 / 0
        return
    finally:
        output.append(6)
        output.append(7)
    output.append(8)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_in_nested_finally_2()
