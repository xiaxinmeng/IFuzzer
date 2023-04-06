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

def test_if_else():
    snippet = '\nif x:\n    a\nelif y:\n    b\nelse:\n    c\n'
    TestExpressionStackSize.check_stack_size(snippet)

TestExpressionStackSize = test_compile.TestExpressionStackSize()
test_if_else()
