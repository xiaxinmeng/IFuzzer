import os
import unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink

import test_msilib

def test_database_open_failed():
    with MsiDatabaseTestCase.assertRaises(msilib.MSIError) as cm:
        msilib.OpenDatabase('non-existent.msi', msilib.MSIDBOPEN_READONLY)
    MsiDatabaseTestCase.assertEqual(str(cm.exception), 'open failed')

MsiDatabaseTestCase = test_msilib.MsiDatabaseTestCase()
test_database_open_failed()
