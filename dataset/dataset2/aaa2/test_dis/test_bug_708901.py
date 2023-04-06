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

def test_bug_708901():
    DisTests.do_disassembly_test(test_dis.bug708901, test_dis.dis_bug708901)

DisTests = test_dis.DisTests()
test_bug_708901()
