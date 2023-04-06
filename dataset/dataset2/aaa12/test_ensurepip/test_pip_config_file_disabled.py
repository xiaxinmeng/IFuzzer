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

def test_pip_config_file_disabled():
    with test_ensurepip.fake_pip():
        ensurepip._uninstall_helper()
    TestBootstrap.assertEqual(TestBootstrap.os_environ['PIP_CONFIG_FILE'], os.devnull)

TestBootstrap = test_ensurepip.TestBootstrap()
TestBootstrap.setUp()
test_pip_config_file_disabled()
