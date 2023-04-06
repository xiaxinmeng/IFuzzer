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

def test_uninstall_version():
    with test.support.captured_stdout() as stdout:
        with TestUninstallationMainFunction.assertRaises(SystemExit):
            ensurepip._uninstall._main(['--version'])
    result = stdout.getvalue().strip()
    TestUninstallationMainFunction.assertEqual(result, test_ensurepip.EXPECTED_VERSION_OUTPUT)
    TestUninstallationMainFunction.assertFalse(TestUninstallationMainFunction.run_pip.called)

TestUninstallationMainFunction = test_ensurepip.TestUninstallationMainFunction()
TestUninstallationMainFunction.setUp()
test_uninstall_version()
