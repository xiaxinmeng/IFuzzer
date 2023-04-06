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

def test_widths():
    for (opcode, opname) in enumerate(dis.opname):
        if opname in ('BUILD_MAP_UNPACK_WITH_CALL', 'BUILD_TUPLE_UNPACK_WITH_CALL', 'JUMP_IF_NOT_EXC_MATCH'):
            continue
        with DisTests.subTest(opname=opname):
            width = dis._OPNAME_WIDTH
            if opcode < dis.HAVE_ARGUMENT:
                width += 1 + dis._OPARG_WIDTH
            DisTests.assertLessEqual(len(opname), width)

DisTests = test_dis.DisTests()
test_widths()
