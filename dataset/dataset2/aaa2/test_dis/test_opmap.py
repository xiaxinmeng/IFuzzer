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

def test_opmap():
    DisTests.assertEqual(dis.opmap['NOP'], 9)
    DisTests.assertIn(dis.opmap['LOAD_CONST'], dis.hasconst)
    DisTests.assertIn(dis.opmap['STORE_NAME'], dis.hasname)

DisTests = test_dis.DisTests()
test_opmap()
