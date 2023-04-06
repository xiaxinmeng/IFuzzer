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

def test_nested():
    with captured_stdout():
        f = test_dis.outer()
    actual = dis.get_instructions(f, first_line=test_dis.expected_f_line)
    InstructionTests.assertEqual(list(actual), test_dis.expected_opinfo_f)

InstructionTests = test_dis.InstructionTests()
test_nested()
