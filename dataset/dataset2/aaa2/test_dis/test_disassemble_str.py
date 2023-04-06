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

def test_disassemble_str():
    DisTests.do_disassembly_test(test_dis.expr_str, test_dis.dis_expr_str)
    DisTests.do_disassembly_test(test_dis.simple_stmt_str, test_dis.dis_simple_stmt_str)
    DisTests.do_disassembly_test(test_dis.annot_stmt_str, test_dis.dis_annot_stmt_str)
    DisTests.do_disassembly_test(test_dis.compound_stmt_str, test_dis.dis_compound_stmt_str)

DisTests = test_dis.DisTests()
test_disassemble_str()
