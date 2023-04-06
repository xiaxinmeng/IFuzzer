import unittest
from test.support import import_helper
import test_dict_version

def test_constructor():
    empty1 = DictVersionTests.new_dict()
    empty2 = DictVersionTests.new_dict()
    empty3 = DictVersionTests.new_dict()
    nonempty1 = DictVersionTests.new_dict(x='x')
    nonempty2 = DictVersionTests.new_dict(x='x', y='y')

DictVersionTests = test_dict_version.DictVersionTests()
DictVersionTests.setUp()
test_constructor()
