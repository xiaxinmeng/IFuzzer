import unittest
from test.support import import_helper
import test_dict_version

def test_setdefault():
    d = DictVersionTests.new_dict()
    DictVersionTests.check_version_changed(d, d.setdefault, 'key', 'value1')
    DictVersionTests.check_version_dont_change(d, d.setdefault, 'key', 'value2')

DictVersionTests = test_dict_version.DictVersionTests()
DictVersionTests.setUp()
test_setdefault()
