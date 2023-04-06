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

def test_instantiation():
    for obj in [test_dis._f, test_dis._C(1).__init__, 'a=1', test_dis._f.__code__]:
        with BytecodeTests.subTest(obj=obj):
            b = dis.Bytecode(obj)
            BytecodeTests.assertIsInstance(b.codeobj, types.CodeType)
    BytecodeTests.assertRaises(TypeError, dis.Bytecode, object())

BytecodeTests = test_dis.BytecodeTests()
test_instantiation()
