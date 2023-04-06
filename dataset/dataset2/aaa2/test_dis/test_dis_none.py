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

def test_dis_none():
    try:
        del sys.last_traceback
    except AttributeError:
        pass
    DisTests.assertRaises(RuntimeError,dis.dis, None)

DisTests = test_dis.DisTests()
test_dis_none()
