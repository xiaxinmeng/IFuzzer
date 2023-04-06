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

def test_basic_bootstrapping():
    exit_code = ensurepip._main([])
    TestBootstrap.run_pip.assert_called_once_with(['install', '--no-cache-dir', '--no-index', '--find-links', unittest.mock.ANY, 'setuptools', 'pip'], unittest.mock.ANY)
    additional_paths = TestBootstrap.run_pip.call_args[0][1]
    TestBootstrap.assertEqual(len(additional_paths), 2)
    TestBootstrap.assertEqual(exit_code, 0)

TestBootstrap = test_ensurepip.TestBootstrap()
TestBootstrap.setUp()
test_basic_bootstrapping()
