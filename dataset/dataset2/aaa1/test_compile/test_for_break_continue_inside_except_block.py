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

def test_for_break_continue_inside_except_block():
    snippet = '\n            for x in y:\n                try:\n                    t\n                except:\n                    if z:\n                        break\n                    elif u:\n                        continue\n                    else:\n                        a\n            else:\n                b\n            '
    TestStackSizeStability.check_stack_size(snippet)

TestStackSizeStability = test_compile.TestStackSizeStability()
test_for_break_continue_inside_except_block()
