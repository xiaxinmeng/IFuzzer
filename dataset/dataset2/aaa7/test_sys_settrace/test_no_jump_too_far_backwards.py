from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(2, -2, [1], (ValueError, 'before'))
def test_no_jump_too_far_backwards(output):
    output.append(1)
    output.append(2)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_too_far_backwards()
