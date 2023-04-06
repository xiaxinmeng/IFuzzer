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

def test_opname():
    DisTests.assertEqual(dis.opname[dis.opmap['LOAD_FAST']], 'LOAD_FAST')

DisTests = test_dis.DisTests()
test_opname()
