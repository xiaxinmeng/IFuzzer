import os
import unittest
from test.support import import_helper
import test_spwd

def test_getspnam_exception():
    name = 'bin'
    try:
        with TestSpwdNonRoot.assertRaises(PermissionError) as cm:
            test_spwd.spwd.getspnam(name)
    except KeyError as exc:
        TestSpwdNonRoot.skipTest("spwd entry %r doesn't exist: %s" % (name, exc))

TestSpwdNonRoot = test_spwd.TestSpwdNonRoot()
test_getspnam_exception()
