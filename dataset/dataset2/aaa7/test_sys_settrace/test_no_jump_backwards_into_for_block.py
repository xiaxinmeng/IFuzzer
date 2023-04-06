from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 2, [2, 2], (ValueError, 'into'))
def test_no_jump_backwards_into_for_block(output):
    for i in (1, 2):
        output.append(2)
    output.append(3)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_backwards_into_for_block()
