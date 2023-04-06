import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

def test_error():
    AnyDBMTestCase.assertTrue(issubclass(AnyDBMTestCase.module.error, OSError))

AnyDBMTestCase = test_dbm.AnyDBMTestCase()
AnyDBMTestCase.setUp()
test_error()
