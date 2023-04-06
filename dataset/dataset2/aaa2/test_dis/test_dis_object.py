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

def test_dis_object():
    DisTests.assertRaises(TypeError, dis.dis, object())

DisTests = test_dis.DisTests()
test_dis_object()
