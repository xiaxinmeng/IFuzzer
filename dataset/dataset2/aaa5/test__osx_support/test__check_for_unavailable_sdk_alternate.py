import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test__check_for_unavailable_sdk_alternate():
    config_vars = {'CC': 'clang', 'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  -isysroot/Developer/SDKs/MacOSX10.1.sdk', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I. -isysroot/Developer/SDKs/MacOSX10.1.sdk', 'BLDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -g', 'LDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -isysroot/Developer/SDKs/MacOSX10.1.sdk -g'}
    expected_vars = {'CC': 'clang', 'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386   ', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I.  ', 'BLDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -g', 'LDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386  -g'}
    Test_OSXSupport.add_expected_saved_initial_values(config_vars, expected_vars)
    Test_OSXSupport.assertEqual(expected_vars, _osx_support._check_for_unavailable_sdk(config_vars))

Test_OSXSupport = test__osx_support.Test_OSXSupport()
test__check_for_unavailable_sdk_alternate()
