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

def test_from_traceback_dis():
    tb = test_dis.get_tb()
    b = dis.Bytecode.from_traceback(tb)
    BytecodeTests.assertEqual(b.dis(), test_dis.dis_traceback)

BytecodeTests = test_dis.BytecodeTests()
test_from_traceback_dis()
