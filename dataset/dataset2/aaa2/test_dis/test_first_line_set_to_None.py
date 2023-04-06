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

def test_first_line_set_to_None():
    actual = dis.get_instructions(test_dis.simple, first_line=None)
    InstructionTests.assertEqual(list(actual), test_dis.expected_opinfo_simple)

InstructionTests = test_dis.InstructionTests()
test_first_line_set_to_None()
