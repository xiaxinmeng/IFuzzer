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

def test_altinstall_default_pip_conflict():
    with TestBootstrap.assertRaises(ValueError):
        ensurepip.bootstrap(altinstall=True, default_pip=True)
    TestBootstrap.assertFalse(TestBootstrap.run_pip.called)

TestBootstrap = test_ensurepip.TestBootstrap()
TestBootstrap.setUp()
test_altinstall_default_pip_conflict()
