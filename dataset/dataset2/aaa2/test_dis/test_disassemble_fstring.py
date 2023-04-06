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

def test_disassemble_fstring():
    DisTests.do_disassembly_test(test_dis._fstring, test_dis.dis_fstring)

DisTests = test_dis.DisTests()
test_disassemble_fstring()
