import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test__remove_universal_flags_alternate():
    config_vars = {'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  ', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I. -isysroot/Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -g', 'LDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -isysroot/Developer/SDKs/MacOSX10.4u.sdk -g'}
    expected_vars = {'CFLAGS': '-fno-strict-aliasing  -g -O3    ', 'LDFLAGS': '    -g', 'CPPFLAGS': '-I.  ', 'BLDSHARED': 'gcc-4.0 -bundle    -g', 'LDSHARED': 'gcc-4.0 -bundle      -g'}
    Test_OSXSupport.add_expected_saved_initial_values(config_vars, expected_vars)
    Test_OSXSupport.assertEqual(expected_vars, _osx_support._remove_universal_flags(config_vars))

Test_OSXSupport = test__osx_support.Test_OSXSupport()
test__remove_universal_flags_alternate()
