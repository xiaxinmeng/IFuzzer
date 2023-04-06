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

def test_dict_evaluation_order():
    i = 0

    def f():
        nonlocal i
        i += 1
        return i
    d = {f(): f(), f(): f()}
    TestSpecifics.assertEqual(d, {1: 2, 3: 4})

TestSpecifics = test_compile.TestSpecifics()
test_dict_evaluation_order()
