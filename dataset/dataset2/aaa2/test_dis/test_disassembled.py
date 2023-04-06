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

def test_disassembled():
    actual = dis.Bytecode(test_dis._f).dis()
    BytecodeTests.assertEqual(actual, test_dis.dis_f)

BytecodeTests = test_dis.BytecodeTests()
test_disassembled()
