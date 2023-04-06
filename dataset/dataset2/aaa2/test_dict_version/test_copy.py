import unittest
from test.support import import_helper
import test_dict_version

def test_copy():
    d = DictVersionTests.new_dict(a=1, b=2)
    d2 = DictVersionTests.check_version_dont_change(d, d.copy)
    DictVersionTests.check_version_unique(d2)

DictVersionTests = test_dict_version.DictVersionTests()
DictVersionTests.setUp()
test_copy()
