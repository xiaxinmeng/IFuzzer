import atexit
import os
import sys
import textwrap
import unittest
from test import support
from test.support import script_helper
import test_atexit

def test_general():
    script = support.findfile('_test_atexit.py')
    script_helper.run_test_script(script)

GeneralTest = test_atexit.GeneralTest()
test_general()
