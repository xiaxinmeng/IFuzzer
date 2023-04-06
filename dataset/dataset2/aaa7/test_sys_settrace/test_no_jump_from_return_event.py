from test import support
import unittest
import sys
import difflib
import gc
from functools import wraps
import asyncio
import gc
import test_sys_settrace

@jump_test(2, 1, [1], event='return', error=(ValueError, "can only jump from a 'line' trace event"))
def test_no_jump_from_return_event(output):
    output.append(1)
    return

JumpTestCase = test_sys_settrace.JumpTestCase()
test_no_jump_from_return_event()
