from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(1, 7, [7, 8])
def test_jump_over_for_block_before_else(output):
    output.append(1)
    if not output:
        for i in [3]:
            output.append(4)
    else:
        output.append(6)
        output.append(7)
    output.append(8)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_over_for_block_before_else()
