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

def test_annotation_limit():
    s = 'def f(%s): pass'
    s %= ', '.join(('a%d:%d' % (i, i) for i in range(300)))
    compile(s, '?', 'exec')

TestSpecifics = test_compile.TestSpecifics()
test_annotation_limit()
