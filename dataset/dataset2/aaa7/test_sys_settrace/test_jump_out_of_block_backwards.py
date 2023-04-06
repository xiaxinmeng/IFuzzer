from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(6, 1, [1, 3, 5, 1, 3, 5, 6, 7])
def test_jump_out_of_block_backwards(output):
    output.append(1)
    for i in [1]:
        output.append(3)
        for j in [2]:
            output.append(5)
        output.append(6)
    output.append(7)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_out_of_block_backwards()
