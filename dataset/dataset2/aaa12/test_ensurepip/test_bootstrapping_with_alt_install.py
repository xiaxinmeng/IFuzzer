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

def test_bootstrapping_with_alt_install():
    ensurepip.bootstrap(altinstall=True)
    TestBootstrap.assertEqual(TestBootstrap.os_environ['ENSUREPIP_OPTIONS'], 'altinstall')

TestBootstrap = test_ensurepip.TestBootstrap()
TestBootstrap.setUp()
test_bootstrapping_with_alt_install()
