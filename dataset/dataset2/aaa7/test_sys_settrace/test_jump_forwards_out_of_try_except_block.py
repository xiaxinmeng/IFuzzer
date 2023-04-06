from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(2, 6, [6])
def test_jump_forwards_out_of_try_except_block(output):
    try:
        output.append(2)
    except:
        output.append(4)
        raise
    output.append(6)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_forwards_out_of_try_except_block()
