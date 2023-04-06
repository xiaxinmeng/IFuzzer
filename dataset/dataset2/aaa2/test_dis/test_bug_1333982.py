from test.support import captured_stdout
from test.support.bytecode_helper import BytecodeTestCase
import unittest
import sys
import dis
import io
import re
import types
import contextlib
from test import dis_module
import test_dis

def test_bug_1333982():
    if not __debug__:
        DisTests.skipTest('need asserts, run without -O')
    DisTests.do_disassembly_test(test_dis.bug1333982, test_dis.dis_bug1333982)

DisTests = test_dis.DisTests()
test_bug_1333982()
