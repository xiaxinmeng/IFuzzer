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

def test_uninstall_error_code():
    with test_ensurepip.fake_pip():
        TestUninstallationMainFunction.run_pip.return_value = 2
        exit_code = ensurepip._uninstall._main([])
    TestUninstallationMainFunction.assertEqual(exit_code, 2)

TestUninstallationMainFunction = test_ensurepip.TestUninstallationMainFunction()
TestUninstallationMainFunction.setUp()
test_uninstall_error_code()
