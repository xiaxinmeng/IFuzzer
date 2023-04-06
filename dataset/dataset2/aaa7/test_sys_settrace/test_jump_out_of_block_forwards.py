from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 5, [2, 5])
def test_jump_out_of_block_forwards(output):
    for i in (1, 2):
        output.append(2)
        for j in [3]:
            output.append(4)
    output.append(5)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_out_of_block_forwards()
