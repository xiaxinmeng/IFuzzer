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

def test_nonascii_abspath():
    if os_helper.TESTFN_UNDECODABLE and sys.platform not in ('win32', 'darwin'):
        name = os_helper.TESTFN_UNDECODABLE
    elif os_helper.TESTFN_NONASCII:
        name = os_helper.TESTFN_NONASCII
    else:
        CommonTest.skipTest('need os_helper.TESTFN_NONASCII')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        with os_helper.temp_cwd(name):
            CommonTest.test_abspath()

CommonTest = test_genericpath.CommonTest()
test_nonascii_abspath()
