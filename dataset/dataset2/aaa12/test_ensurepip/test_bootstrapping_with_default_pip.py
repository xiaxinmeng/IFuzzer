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

def test_bootstrapping_with_default_pip():
    ensurepip.bootstrap(default_pip=True)
    TestBootstrap.assertNotIn('ENSUREPIP_OPTIONS', TestBootstrap.os_environ)

TestBootstrap = test_ensurepip.TestBootstrap()
TestBootstrap.setUp()
test_bootstrapping_with_default_pip()
