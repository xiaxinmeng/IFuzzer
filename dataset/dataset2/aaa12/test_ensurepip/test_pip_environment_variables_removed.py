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

def test_pip_environment_variables_removed():
    TestBootstrap.os_environ['PIP_THIS_SHOULD_GO_AWAY'] = 'test fodder'
    with test_ensurepip.fake_pip():
        ensurepip._uninstall_helper()
    TestBootstrap.assertNotIn('PIP_THIS_SHOULD_GO_AWAY', TestBootstrap.os_environ)

TestBootstrap = test_ensurepip.TestBootstrap()
TestBootstrap.setUp()
test_pip_environment_variables_removed()
