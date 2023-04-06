from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 1, [1, 1, 3])
def test_jump_backwards_out_of_try_except_block(output):
    output.append(1)
    try:
        output.append(3)
    except:
        output.append(5)
        raise

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_backwards_out_of_try_except_block()
