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

def test_code_info_object():
    CodeInfoTests.assertRaises(TypeError, dis.code_info, object())

CodeInfoTests = test_dis.CodeInfoTests()
test_code_info_object()
