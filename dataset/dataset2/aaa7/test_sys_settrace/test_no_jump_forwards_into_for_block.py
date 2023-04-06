from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(1, 3, [], (ValueError, 'into'))
def test_no_jump_forwards_into_for_block(output):
    output.append(1)
    for i in (1, 2):
        output.append(3)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_forwards_into_for_block()
