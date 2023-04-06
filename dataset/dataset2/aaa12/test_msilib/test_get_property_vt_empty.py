import os
import unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink

import test_msilib

def test_get_property_vt_empty():
    (db, db_path) = init_database()
    summary = db.GetSummaryInformation(0)
    MsiDatabaseTestCase.assertIsNone(summary.GetProperty(msilib.PID_SECURITY))
    db.Close()
    MsiDatabaseTestCase.addCleanup(unlink, db_path)

MsiDatabaseTestCase = test_msilib.MsiDatabaseTestCase()
test_get_property_vt_empty()
