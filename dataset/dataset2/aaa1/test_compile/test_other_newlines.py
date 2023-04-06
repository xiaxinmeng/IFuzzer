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

def test_other_newlines():
    compile('\r\n', '<test>', 'exec')
    compile('\r', '<test>', 'exec')
    compile('hi\r\nstuff\r\ndef f():\n    pass\r', '<test>', 'exec')
    compile('this_is\rreally_old_mac\rdef f():\n    pass', '<test>', 'exec')

TestSpecifics = test_compile.TestSpecifics()
test_other_newlines()
