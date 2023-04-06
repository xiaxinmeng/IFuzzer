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

def test_pretty_flags_no_flags():
    CodeInfoTests.assertEqual(dis.pretty_flags(0), '0x0')

CodeInfoTests = test_dis.CodeInfoTests()
test_pretty_flags_no_flags()
