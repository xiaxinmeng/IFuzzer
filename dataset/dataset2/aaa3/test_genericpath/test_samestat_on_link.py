import genericpath
import os
import sys
import unittest
import warnings
from test.support import os_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_ok
from test.support.os_helper import FakePath
import test_genericpath

def test_samestat_on_link():
    try:
        GenericTest._test_samestat_on_link_func(os.link)
    except PermissionError as e:
        GenericTest.skipTest('os.link(): %s' % e)

GenericTest = test_genericpath.GenericTest()
test_samestat_on_link()
