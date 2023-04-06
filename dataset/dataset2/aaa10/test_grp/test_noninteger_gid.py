import unittest
from test.support import import_helper
import test_grp

def test_noninteger_gid():
    entries = test_grp.grp.getgrall()
    if not entries:
        GroupDatabaseTestCase.skipTest('no groups')
    gid = entries[0][2]
    GroupDatabaseTestCase.assertRaises(TypeError, test_grp.grp.getgrgid, float(gid))
    GroupDatabaseTestCase.assertRaises(TypeError, test_grp.grp.getgrgid, str(gid))

GroupDatabaseTestCase = test_grp.GroupDatabaseTestCase()
test_noninteger_gid()
