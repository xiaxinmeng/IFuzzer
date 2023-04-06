import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test__override_all_archs():
    Test_OSXSupport.env['ARCHFLAGS'] = '-arch x86_64'
    config_vars = {'CC': 'clang', 'CFLAGS': '-fno-strict-aliasing  -g -O3 -arch ppc -arch i386  ', 'LDFLAGS': '-arch ppc -arch i386   -g', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-4.0 -bundle  -arch ppc -arch i386 -g', 'LDSHARED': 'gcc-4.0 -bundle -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g'}
    expected_vars = {'CC': 'clang', 'CFLAGS': '-fno-strict-aliasing  -g -O3     -arch x86_64', 'LDFLAGS': '    -g -arch x86_64', 'CPPFLAGS': '-I. -isysroot /Developer/SDKs/MacOSX10.4u.sdk', 'BLDSHARED': 'gcc-4.0 -bundle    -g -arch x86_64', 'LDSHARED': 'gcc-4.0 -bundle   -isysroot /Developer/SDKs/MacOSX10.4u.sdk -g -arch x86_64'}
    Test_OSXSupport.add_expected_saved_initial_values(config_vars, expected_vars)
    Test_OSXSupport.assertEqual(expected_vars, _osx_support._override_all_archs(config_vars))

Test_OSXSupport = test__osx_support.Test_OSXSupport()
Test_OSXSupport.setUp()
test__override_all_archs()
