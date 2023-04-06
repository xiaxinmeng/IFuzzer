import unittest
from test.support import import_helper
import test_dict_version

def test_update():
    d = DictVersionTests.new_dict(key='value')
    DictVersionTests.check_version_dont_change(d, d.update)
    DictVersionTests.check_version_changed(d, d.update, key='new value')
    d2 = DictVersionTests.new_dict(key='value 3')
    DictVersionTests.check_version_changed(d, d.update, d2)

DictVersionTests = test_dict_version.DictVersionTests()
DictVersionTests.setUp()
test_update()
