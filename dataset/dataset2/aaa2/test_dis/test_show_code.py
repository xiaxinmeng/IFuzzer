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

def test_show_code():
    CodeInfoTests.maxDiff = 1000
    for (x, expected) in CodeInfoTests.test_pairs:
        with captured_stdout() as output:
            dis.show_code(x)
        CodeInfoTests.assertRegex(output.getvalue(), expected + '\n')
        output = io.StringIO()
        dis.show_code(x, file=output)
        CodeInfoTests.assertRegex(output.getvalue(), expected)

CodeInfoTests = test_dis.CodeInfoTests()
test_show_code()
