import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test__get_system_version():
    Test_OSXSupport.assertTrue(platform.mac_ver()[0].startswith(_osx_support._get_system_version()))

Test_OSXSupport = test__osx_support.Test_OSXSupport()
test__get_system_version()
