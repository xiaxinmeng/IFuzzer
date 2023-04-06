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

def test_from_traceback():
    tb = test_dis.get_tb()
    b = dis.Bytecode.from_traceback(tb)
    while tb.tb_next:
        tb = tb.tb_next
    BytecodeTests.assertEqual(b.current_offset, tb.tb_lasti)

BytecodeTests = test_dis.BytecodeTests()
test_from_traceback()
