from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(1, 2, [3])
def test_jump_to_codeless_line(output):
    output.append(1)
    output.append(3)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_to_codeless_line()
