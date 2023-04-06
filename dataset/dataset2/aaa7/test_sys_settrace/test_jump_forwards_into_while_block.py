from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(2, 4, [4, 4])
def test_jump_forwards_into_while_block(output):
    i = 1
    output.append(2)
    while i <= 2:
        output.append(4)
        i += 1

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_forwards_into_while_block()
