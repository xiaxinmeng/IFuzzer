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

def test_with():
    snippet = '\n            with x as y:\n                a\n            '
    TestStackSizeStability.check_stack_size(snippet)

TestStackSizeStability = test_compile.TestStackSizeStability()
test_with()
