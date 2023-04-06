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

def test_sequence_unpacking_error():
    (i, j) = (1, -1) or (-1, 1)
    TestSpecifics.assertEqual(i, 1)
    TestSpecifics.assertEqual(j, -1)

TestSpecifics = test_compile.TestSpecifics()
test_sequence_unpacking_error()
