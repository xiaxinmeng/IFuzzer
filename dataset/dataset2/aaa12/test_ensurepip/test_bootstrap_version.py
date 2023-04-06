import unittest
import unittest.mock
import test.support
import os
import os.path
import contextlib
import sys
import ensurepip
import ensurepip._uninstall
import test_ensurepip

def test_bootstrap_version():
    with test.support.captured_stdout() as stdout:
        with TestBootstrappingMainFunction.assertRaises(SystemExit):
            ensurepip._main(['--version'])
    result = stdout.getvalue().strip()
    TestBootstrappingMainFunction.assertEqual(result, test_ensurepip.EXPECTED_VERSION_OUTPUT)
    TestBootstrappingMainFunction.assertFalse(TestBootstrappingMainFunction.run_pip.called)

TestBootstrappingMainFunction = test_ensurepip.TestBootstrappingMainFunction()
TestBootstrappingMainFunction.setUp()
test_bootstrap_version()
