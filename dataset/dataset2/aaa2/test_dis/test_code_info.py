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

def test_code_info():
    CodeInfoTests.maxDiff = 1000
    for (x, expected) in CodeInfoTests.test_pairs:
        CodeInfoTests.assertRegex(dis.code_info(x), expected)

CodeInfoTests = test_dis.CodeInfoTests()
test_code_info()
