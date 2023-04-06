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

def test_dis_traceback():
    try:
        del sys.last_traceback
    except AttributeError:
        pass
    try:
        1 / 0
    except Exception as e:
        tb = e.__traceback__
        sys.last_traceback = tb
    tb_dis = DisTests.get_disassemble_as_string(tb.tb_frame.f_code, tb.tb_lasti)
    DisTests.do_disassembly_test(None, tb_dis)

DisTests = test_dis.DisTests()
test_dis_traceback()
