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

def test_explicit_first_line():
    actual = dis.Bytecode(test_dis.outer, first_line=test_dis.expected_outer_line)
    BytecodeTests.assertEqual(list(actual), test_dis.expected_opinfo_outer)

BytecodeTests = test_dis.BytecodeTests()
test_explicit_first_line()
