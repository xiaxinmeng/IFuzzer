import unittest
from test.support import import_helper
import test_dict_version

def test_pop():
    d = DictVersionTests.new_dict(key='value')
    DictVersionTests.check_version_changed(d, d.pop, 'key')
    DictVersionTests.check_version_dont_change(d, DictVersionTests.assertRaises, KeyError, d.pop, 'key')

DictVersionTests = test_dict_version.DictVersionTests()
DictVersionTests.setUp()
test_pop()
