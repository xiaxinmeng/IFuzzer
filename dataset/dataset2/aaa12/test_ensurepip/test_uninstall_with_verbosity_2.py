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

def test_uninstall_with_verbosity_2():
    with test_ensurepip.fake_pip():
        ensurepip._uninstall_helper(verbosity=2)
    TestUninstall.run_pip.assert_called_once_with(['uninstall', '-y', '--disable-pip-version-check', '-vv', 'pip', 'setuptools'])

TestUninstall = test_ensurepip.TestUninstall()
test_uninstall_with_verbosity_2()
