from test.support import import_helper
from test.support import os_helper
import os
import unittest
import dbm.ndbm
from dbm.ndbm import error
import test_dbm_ndbm

def test_modes():
    for mode in ['r', 'rw', 'w', 'n']:
        try:
            DbmTestCase.d = dbm.ndbm.open(DbmTestCase.filename, mode)
            DbmTestCase.d.close()
        except error:
            DbmTestCase.fail()

DbmTestCase = test_dbm_ndbm.DbmTestCase()
test_modes()
