from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 5, [1, 2, 5])
def test_jump_out_of_with_assignment(output):
    output.append(1)
    with tracecontext(output, 2) as x:
        output.append(4)
    output.append(5)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_out_of_with_assignment()
