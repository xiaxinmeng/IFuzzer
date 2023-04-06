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

def test_source_line_in_disassembly():
    actual = dis.Bytecode(test_dis.simple).dis()
    actual = actual.strip().partition(' ')[0]
    expected = str(test_dis.simple.__code__.co_firstlineno)
    BytecodeTests.assertEqual(actual, expected)
    actual = dis.Bytecode(test_dis.simple, first_line=350).dis()
    actual = actual.strip().partition(' ')[0]
    BytecodeTests.assertEqual(actual, '350')

BytecodeTests = test_dis.BytecodeTests()
test_source_line_in_disassembly()
