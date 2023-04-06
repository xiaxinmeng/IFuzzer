from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(4, 9, [2, 9])
def test_jump_in_nested_finally(output):
    try:
        output.append(2)
    finally:
        output.append(4)
        try:
            output.append(6)
        finally:
            output.append(8)
        output.append(9)

JumpTestCase = test_sys_settrace.JumpTestCase()
test_jump_in_nested_finally()
