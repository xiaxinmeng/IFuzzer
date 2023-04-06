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

def test_path_like_objects():
    compile('42', FakePath('test_compile_pathlike'), 'single')

TestSpecifics = test_compile.TestSpecifics()
test_path_like_objects()
