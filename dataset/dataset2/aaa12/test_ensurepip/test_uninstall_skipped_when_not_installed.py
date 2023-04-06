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

def test_uninstall_skipped_when_not_installed():
    with test_ensurepip.fake_pip(None):
        ensurepip._uninstall_helper()
    TestUninstall.assertFalse(TestUninstall.run_pip.called)

TestUninstall = test_ensurepip.TestUninstall()
TestUninstall.setUp()
test_uninstall_skipped_when_not_installed()
