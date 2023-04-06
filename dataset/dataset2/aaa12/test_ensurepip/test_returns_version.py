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

def test_returns_version():
    TestEnsurePipVersion.assertEqual(ensurepip._PIP_VERSION, ensurepip.version())

TestEnsurePipVersion = test_ensurepip.TestEnsurePipVersion()
test_returns_version()
