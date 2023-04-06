import unittest
from test.support import import_helper
import test_dict_version

def test_clear():
    d = DictVersionTests.new_dict(key='value')
    DictVersionTests.check_version_changed(d, d.clear)
    DictVersionTests.check_version_dont_change(d, d.clear)

DictVersionTests = test_dict_version.DictVersionTests()
DictVersionTests.setUp()
test_clear()
