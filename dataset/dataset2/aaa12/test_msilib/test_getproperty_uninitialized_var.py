import os
import unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink

import test_msilib

def test_getproperty_uninitialized_var():
    (db, db_path) = init_database()
    MsiDatabaseTestCase.addCleanup(unlink, db_path)
    MsiDatabaseTestCase.addCleanup(db.Close)
    si = db.GetSummaryInformation(0)
    with MsiDatabaseTestCase.assertRaises(msilib.MSIError):
        si.GetProperty(-1)

MsiDatabaseTestCase = test_msilib.MsiDatabaseTestCase()
test_getproperty_uninitialized_var()
