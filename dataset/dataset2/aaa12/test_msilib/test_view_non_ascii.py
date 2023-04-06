import os
import unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink

import test_msilib

def test_view_non_ascii():
    (db, db_path) = init_database()
    view = db.OpenView("SELECT 'ß-розпад' FROM Property")
    view.Execute(None)
    record = view.Fetch()
    MsiDatabaseTestCase.assertEqual(record.GetString(1), 'ß-розпад')
    view.Close()
    db.Close()
    MsiDatabaseTestCase.addCleanup(unlink, db_path)

MsiDatabaseTestCase = test_msilib.MsiDatabaseTestCase()
test_view_non_ascii()
