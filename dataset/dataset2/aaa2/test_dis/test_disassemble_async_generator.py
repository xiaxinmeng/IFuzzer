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

def test_disassemble_async_generator():
    agen_func_disas = DisTests.get_disassembly(test_dis._ag)
    agen_disas = DisTests.get_disassembly(test_dis._ag(1))
    DisTests.assertEqual(agen_disas, agen_func_disas)

DisTests = test_dis.DisTests()
test_disassemble_async_generator()
