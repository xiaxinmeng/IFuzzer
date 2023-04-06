import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test__supports_universal_builds():
    import platform
    mac_ver_tuple = tuple((int(i) for i in platform.mac_ver()[0].split('.')[0:2]))
    Test_OSXSupport.assertEqual(mac_ver_tuple >= (10, 4), _osx_support._supports_universal_builds())

Test_OSXSupport = test__osx_support.Test_OSXSupport()
test__supports_universal_builds()
