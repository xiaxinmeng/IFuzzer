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

def test_bootstrapping_with_regular_install():
    ensurepip.bootstrap()
    TestBootstrap.assertEqual(TestBootstrap.os_environ['ENSUREPIP_OPTIONS'], 'install')

TestBootstrap = test_ensurepip.TestBootstrap()
TestBootstrap.setUp()
test_bootstrapping_with_regular_install()
