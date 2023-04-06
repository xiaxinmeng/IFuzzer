import os
import unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink
import test_msilib

def test_database_create_failed():
    db_path = os.path.join(TESTFN, 'test.msi')
    with MsiDatabaseTestCase.assertRaises(msilib.MSIError) as cm:
        msilib.OpenDatabase(db_path, msilib.MSIDBOPEN_CREATE)
    MsiDatabaseTestCase.assertEqual(str(cm.exception), 'create failed')

MsiDatabaseTestCase = test_msilib.MsiDatabaseTestCase()
test_database_create_failed()
