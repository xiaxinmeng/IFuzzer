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

def test_disassemble_coroutine():
    coro_func_disas = DisTests.get_disassembly(test_dis._co)
    coro = test_dis._co(1)
    coro.close()
    coro_disas = DisTests.get_disassembly(coro)
    DisTests.assertEqual(coro_disas, coro_func_disas)

DisTests = test_dis.DisTests()
test_disassemble_coroutine()
