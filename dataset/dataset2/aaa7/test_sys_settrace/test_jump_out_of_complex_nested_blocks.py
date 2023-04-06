from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(8, 11, [1, 3, 5, 11, 12])
def test_jump_out_of_complex_nested_blocks(output):
    output.append(1)
    for i in [1]:
        output.append(3)
        for j in [1, 2]:
            output.append(5)
            try:
                for k in [1, 2]:
                    output.append(8)
            finally:
                output.append(10)
        output.append(11)
    output.append(12)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_out_of_complex_nested_blocks()
