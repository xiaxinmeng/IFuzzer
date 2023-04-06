from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(3, 2, [2, 5], event='return')
def test_jump_from_yield(output):

    def gen():
        output.append(2)
        yield 3
    next(gen())
    output.append(5)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_from_yield()
