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

def test_jumpy():
    actual = dis.get_instructions(test_dis.jumpy, first_line=test_dis.expected_jumpy_line)
    InstructionTests.assertEqual(list(actual), test_dis.expected_opinfo_jumpy)

InstructionTests = test_dis.InstructionTests()
test_jumpy()
