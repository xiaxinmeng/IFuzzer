import unittest
from test.support import import_helper
import test_grp

def test_values():
    entries = test_grp.grp.getgrall()
    for e in entries:
        GroupDatabaseTestCase.check_value(e)

GroupDatabaseTestCase = test_grp.GroupDatabaseTestCase()
test_values()
