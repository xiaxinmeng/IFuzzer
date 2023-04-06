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

def test_disassemble_instance_method_bytes():
    method_bytecode = test_dis._C(1).__init__.__code__.co_code
    DisTests.do_disassembly_test(method_bytecode, test_dis.dis_c_instance_method_bytes)

DisTests = test_dis.DisTests()
test_disassemble_instance_method_bytes()
