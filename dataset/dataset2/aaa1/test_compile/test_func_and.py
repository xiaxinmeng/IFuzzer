import dis
import math
import os
import unittest
import sys
import _ast
import tempfile
import types
from test import support
from test.support import script_helper
from test.support.os_helper import FakePath
import builtins

import dis, io
import test_compile

def test_func_and():
    code = 'def f(x):\n'
    code += '   x and x\n' * TestExpressionStackSize.N
    TestExpressionStackSize.check_stack_size(code)

TestExpressionStackSize = test_compile.TestExpressionStackSize()
test_func_and()
