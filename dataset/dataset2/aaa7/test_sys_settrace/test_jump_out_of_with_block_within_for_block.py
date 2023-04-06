from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(4, 5, [1, 3, 5, 6])
def test_jump_out_of_with_block_within_for_block(output):
    output.append(1)
    for i in [1]:
        with tracecontext(output, 3):
            output.append(4)
        output.append(5)
    output.append(6)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_out_of_with_block_within_for_block()
