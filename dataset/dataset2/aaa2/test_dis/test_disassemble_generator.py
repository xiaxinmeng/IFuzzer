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

def test_disassemble_generator():
    gen_func_disas = DisTests.get_disassembly(test_dis._g)
    gen_disas = DisTests.get_disassembly(test_dis._g(1))
    DisTests.assertEqual(gen_disas, gen_func_disas)

DisTests = test_dis.DisTests()
test_disassemble_generator()
