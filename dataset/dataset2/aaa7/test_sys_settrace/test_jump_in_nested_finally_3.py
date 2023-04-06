from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(6, 11, [2, 11], (ZeroDivisionError, ''))
def test_jump_in_nested_finally_3(output):
    try:
        output.append(2)
        1 / 0
        return
    finally:
        output.append(6)
        try:
            output.append(8)
        finally:
            output.append(10)
        output.append(11)
    output.append(12)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_in_nested_finally_3()
