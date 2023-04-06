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

def test_info():
    BytecodeTests.maxDiff = 1000
    for (x, expected) in test_dis.CodeInfoTests.test_pairs:
        b = dis.Bytecode(x)
        BytecodeTests.assertRegex(b.info(), expected)

BytecodeTests = test_dis.BytecodeTests()
test_info()
