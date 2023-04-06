import subprocess
import sys
import os
from test.support import script_helper
import unittest
from unittest import mock
import test_script_helper

@mock.patch('subprocess.check_call')
def test_interpreter_requires_environment_true(TestScriptHelperEnvironment, mock_check_call):
    with mock.patch.dict(os.environ):
        os.environ.pop('PYTHONHOME', None)
        mock_check_call.side_effect = subprocess.CalledProcessError('', '')
        TestScriptHelperEnvironment.assertTrue(script_helper.interpreter_requires_environment())
        TestScriptHelperEnvironment.assertTrue(script_helper.interpreter_requires_environment())
        TestScriptHelperEnvironment.assertEqual(1, mock_check_call.call_count)

TestScriptHelperEnvironment = test_script_helper.TestScriptHelperEnvironment()
test_interpreter_requires_environment_true()
