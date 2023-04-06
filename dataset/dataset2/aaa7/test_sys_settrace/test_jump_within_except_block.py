from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(5, 6, [4, 6, 7])
def test_jump_within_except_block(output):
    try:
        1 / 0
    except:
        output.append(4)
        output.append(5)
        output.append(6)
    output.append(7)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_within_except_block()
