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

def test_boundaries():
    DisTests.assertEqual(dis.opmap['EXTENDED_ARG'], dis.EXTENDED_ARG)
    DisTests.assertEqual(dis.opmap['STORE_NAME'], dis.HAVE_ARGUMENT)

DisTests = test_dis.DisTests()
test_boundaries()
