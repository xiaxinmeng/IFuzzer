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

def test_bootstrapping_error_code():
    TestBootstrappingMainFunction.run_pip.return_value = 2
    exit_code = ensurepip._main([])
    TestBootstrappingMainFunction.assertEqual(exit_code, 2)

TestBootstrappingMainFunction = test_ensurepip.TestBootstrappingMainFunction()
TestBootstrappingMainFunction.setUp()
test_bootstrapping_error_code()
