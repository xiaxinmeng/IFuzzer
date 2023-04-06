import unittest
from test.support import import_helper
import test_dict_version

def test_setitem():
    d = DictVersionTests.new_dict()
    DictVersionTests.check_version_changed(d, d.__setitem__, 'x', 'x')
    DictVersionTests.check_version_changed(d, d.__setitem__, 'y', 'y')
    DictVersionTests.check_version_changed(d, d.__setitem__, 'x', 1)
    DictVersionTests.check_version_changed(d, d.__setitem__, 'y', 2)

DictVersionTests = test_dict_version.DictVersionTests()
DictVersionTests.setUp()
test_setitem()
