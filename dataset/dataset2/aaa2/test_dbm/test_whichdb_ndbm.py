import unittest
import glob
from test.support import import_helper
from test.support import os_helper
from dbm import ndbm
import test_dbm

@unittest.skipUnless(ndbm, reason='Test requires ndbm')
def test_whichdb_ndbm():
    db_file = '{}_ndbm.db'.format(test_dbm._fname)
    with open(db_file, 'w'):
        WhichDBTestCase.addCleanup(os_helper.unlink, db_file)
    WhichDBTestCase.assertIsNone(WhichDBTestCase.dbm.whichdb(db_file[:-3]))

WhichDBTestCase = test_dbm.WhichDBTestCase()
test_whichdb_ndbm()
