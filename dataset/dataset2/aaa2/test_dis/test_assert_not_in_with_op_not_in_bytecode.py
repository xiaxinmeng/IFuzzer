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

def test_assert_not_in_with_op_not_in_bytecode():
    code = compile('a = 1', '<string>', 'exec')
    TestBytecodeTestCase.assertInBytecode(code, 'LOAD_CONST', 1)
    TestBytecodeTestCase.assertNotInBytecode(code, 'LOAD_NAME')
    TestBytecodeTestCase.assertNotInBytecode(code, 'LOAD_NAME', 'a')

TestBytecodeTestCase = test_dis.TestBytecodeTestCase()
test_assert_not_in_with_op_not_in_bytecode()
