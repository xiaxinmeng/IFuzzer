from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(7, 1, [1, 3, 6], (ValueError, "out of an 'except'"))
def test_no_jump_out_of_qualified_except_block(output):
    output.append(1)
    try:
        output.append(3)
        1 / 0
    except Exception:
        output.append(6)
        output.append(7)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_out_of_qualified_except_block()
