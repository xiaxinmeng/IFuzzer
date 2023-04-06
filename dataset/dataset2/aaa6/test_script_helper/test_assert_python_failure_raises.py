import subprocess
import sys
import os
from test.support import script_helper
import unittest
from unittest import mock
import test_script_helper

def test_assert_python_failure_raises():
    with TestScriptHelper.assertRaises(AssertionError) as error_context:
        script_helper.assert_python_failure('-c', 'import sys; sys.exit(0)')
    error_msg = str(error_context.exception)
    TestScriptHelper.assertIn('Process return code is 0\n', error_msg)
    TestScriptHelper.assertIn('import sys; sys.exit(0)', error_msg, msg='unexpected command line.')

TestScriptHelper = test_script_helper.TestScriptHelper()
test_assert_python_failure_raises()
