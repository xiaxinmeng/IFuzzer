import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test_get_platform_osx():
    config_vars = {'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  -isysroot /Developer/SDKs/MacOSX10.1.sdk', 'MACOSX_DEPLOYMENT_TARGET': '10.6'}
    result = _osx_support.get_platform_osx(config_vars, ' ', ' ', ' ')
    Test_OSXSupport.assertEqual(('macosx', '10.6', 'fat'), result)

Test_OSXSupport = test__osx_support.Test_OSXSupport()
test_get_platform_osx()
