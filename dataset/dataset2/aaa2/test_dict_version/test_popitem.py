import unittest
from test.support import import_helper
import test_dict_version

def test_popitem():
    d = DictVersionTests.new_dict(key='value')
    DictVersionTests.check_version_changed(d, d.popitem)
    DictVersionTests.check_version_dont_change(d, DictVersionTests.assertRaises, KeyError, d.popitem)

DictVersionTests = test_dict_version.DictVersionTests()
DictVersionTests.setUp()
test_popitem()
