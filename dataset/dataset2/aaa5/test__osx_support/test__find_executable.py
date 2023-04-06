import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test__find_executable():
    if Test_OSXSupport.env['PATH']:
        Test_OSXSupport.env['PATH'] = Test_OSXSupport.env['PATH'] + ':'
    Test_OSXSupport.env['PATH'] = Test_OSXSupport.env['PATH'] + os.path.abspath(Test_OSXSupport.temp_path_dir)
    os_helper.unlink(Test_OSXSupport.prog_name)
    Test_OSXSupport.assertIsNone(_osx_support._find_executable(Test_OSXSupport.prog_name))
    Test_OSXSupport.addCleanup(os_helper.unlink, Test_OSXSupport.prog_name)
    with open(Test_OSXSupport.prog_name, 'w') as f:
        f.write('#!/bin/sh\n/bin/echo OK\n')
    os.chmod(Test_OSXSupport.prog_name, stat.S_IRWXU)
    Test_OSXSupport.assertEqual(Test_OSXSupport.prog_name, _osx_support._find_executable(Test_OSXSupport.prog_name))

Test_OSXSupport = test__osx_support.Test_OSXSupport()
Test_OSXSupport.setUp()
test__find_executable()
