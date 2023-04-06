import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test__find_build_tool():
    out = _osx_support._find_build_tool('cc')
    Test_OSXSupport.assertTrue(os.path.isfile(out), 'cc not found - check xcode-select')

Test_OSXSupport = test__osx_support.Test_OSXSupport()
test__find_build_tool()
