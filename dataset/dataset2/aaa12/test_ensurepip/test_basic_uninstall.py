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

def test_basic_uninstall():
    with test_ensurepip.fake_pip():
        exit_code = ensurepip._uninstall._main([])
    TestUninstallationMainFunction.run_pip.assert_called_once_with(['uninstall', '-y', '--disable-pip-version-check', 'pip', 'setuptools'])
    TestUninstallationMainFunction.assertEqual(exit_code, 0)

TestUninstallationMainFunction = test_ensurepip.TestUninstallationMainFunction()
test_basic_uninstall()
