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

def test_stack_overflow():
    compile('if a: b\n' * 200000, '<dummy>', 'exec')

TestSpecifics = test_compile.TestSpecifics()
test_stack_overflow()
