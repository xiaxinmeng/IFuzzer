from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(5, 3, [3, 3, 3, 5])
def test_jump_backwards_into_while_block(output):
    i = 1
    while i <= 2:
        output.append(3)
        i += 1
    output.append(5)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_backwards_into_while_block()
