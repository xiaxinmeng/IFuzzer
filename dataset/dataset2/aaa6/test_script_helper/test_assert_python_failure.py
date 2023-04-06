import subprocess
import sys
import os
from test.support import script_helper
import unittest
from unittest import mock
import test_script_helper

def test_assert_python_failure():
    (rc, out, err) = script_helper.assert_python_failure('-c', 'sys.exit(0)')
    TestScriptHelper.assertNotEqual(0, rc, 'return code should not be 0')

TestScriptHelper = test_script_helper.TestScriptHelper()
test_assert_python_failure()
