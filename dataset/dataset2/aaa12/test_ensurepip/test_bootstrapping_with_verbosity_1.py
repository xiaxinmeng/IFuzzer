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

def test_bootstrapping_with_verbosity_1():
    ensurepip.bootstrap(verbosity=1)
    TestBootstrap.run_pip.assert_called_once_with(['install', '--no-cache-dir', '--no-index', '--find-links', unittest.mock.ANY, '-v', 'setuptools', 'pip'], unittest.mock.ANY)

TestBootstrap = test_ensurepip.TestBootstrap()
TestBootstrap.setUp()
test_bootstrapping_with_verbosity_1()
