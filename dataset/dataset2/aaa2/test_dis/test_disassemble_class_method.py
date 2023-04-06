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

def test_disassemble_class_method():
    DisTests.do_disassembly_test(test_dis._C.cm, test_dis.dis_c_class_method)

DisTests = test_dis.DisTests()
test_disassemble_class_method()
