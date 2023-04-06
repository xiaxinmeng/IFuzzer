import subprocess
import sys
import os
from test.support import script_helper
import unittest
from unittest import mock
import test_script_helper

def test_assert_python_ok():
    t = script_helper.assert_python_ok('-c', 'import sys; sys.exit(0)')
    TestScriptHelper.assertEqual(0, t[0], 'return code was not 0')

TestScriptHelper = test_script_helper.TestScriptHelper()
test_assert_python_ok()
