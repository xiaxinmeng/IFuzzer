from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(5, 7, [4], (ValueError, 'into'))
def test_no_jump_between_except_blocks_2(output):
    try:
        1 / 0
    except ZeroDivisionError:
        output.append(4)
        output.append(5)
    except FloatingPointError as e:
        output.append(7)
    output.append(8)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_between_except_blocks_2()
