from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 4, [1], (ValueError, 'after'))
def test_no_jump_infinite_while_loop(output):
    output.append(1)
    while True:
        output.append(3)
    output.append(4)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_infinite_while_loop()
