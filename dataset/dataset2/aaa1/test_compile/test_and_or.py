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

def test_and_or():
    TestExpressionStackSize.check_stack_size('x and x or ' * TestExpressionStackSize.N + 'x')

TestExpressionStackSize = test_compile.TestExpressionStackSize()
test_and_or()
