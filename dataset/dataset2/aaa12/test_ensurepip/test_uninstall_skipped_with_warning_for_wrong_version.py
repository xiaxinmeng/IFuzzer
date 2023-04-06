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

def test_uninstall_skipped_with_warning_for_wrong_version():
    with test_ensurepip.fake_pip('not a valid version'):
        with test.support.captured_stderr() as stderr:
            ensurepip._uninstall_helper()
    warning = stderr.getvalue().strip()
    TestUninstall.assertIn('only uninstall a matching version', warning)
    TestUninstall.assertFalse(TestUninstall.run_pip.called)

TestUninstall = test_ensurepip.TestUninstall()
TestUninstall.setUp()
test_uninstall_skipped_with_warning_for_wrong_version()
