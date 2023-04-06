from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(2, 3, [4], (ValueError, 'except'))
def test_no_jump_to_except_3(output):
    try:
        output.append(2)
    except ValueError as e:
        output.append(4)
        raise e

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_to_except_3()
