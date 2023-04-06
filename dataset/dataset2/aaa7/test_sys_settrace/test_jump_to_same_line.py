from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(2, 2, [1, 2, 3])
def test_jump_to_same_line(output):
    output.append(1)
    output.append(2)
    output.append(3)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_to_same_line()
