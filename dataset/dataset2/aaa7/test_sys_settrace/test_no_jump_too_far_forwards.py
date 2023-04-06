from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(2, 3, [1], (ValueError, 'after'))
def test_no_jump_too_far_forwards(output):
    output.append(1)
    output.append(2)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_too_far_forwards()
