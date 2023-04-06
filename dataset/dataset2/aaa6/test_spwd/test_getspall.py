import os
import unittest
from test.support import import_helper
import test_spwd

def test_getspall():
    entries = test_spwd.spwd.getspall()
    TestSpwdRoot.assertIsInstance(entries, list)
    for entry in entries:
        TestSpwdRoot.assertIsInstance(entry, test_spwd.spwd.struct_spwd)

TestSpwdRoot = test_spwd.TestSpwdRoot()
test_getspall()
