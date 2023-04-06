from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 6, [2, 5, 6], (ValueError, "into an 'except'"))
def test_no_jump_into_bare_except_block_from_try_block(output):
    try:
        output.append(2)
        output.append(3)
    except:
        output.append(5)
        output.append(6)
        raise
    output.append(8)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_into_bare_except_block_from_try_block()
