import os
import platform
import stat
import sys
import unittest
from test.support import os_helper
import _osx_support
import platform
import test__osx_support

def test__read_output():
    if Test_OSXSupport.env['PATH']:
        Test_OSXSupport.env['PATH'] = Test_OSXSupport.env['PATH'] + ':'
    Test_OSXSupport.env['PATH'] = Test_OSXSupport.env['PATH'] + os.path.abspath(Test_OSXSupport.temp_path_dir)
    os_helper.unlink(Test_OSXSupport.prog_name)
    Test_OSXSupport.addCleanup(os_helper.unlink, Test_OSXSupport.prog_name)
    with open(Test_OSXSupport.prog_name, 'w') as f:
        f.write('#!/bin/sh\n/bin/echo ExpectedOutput\n')
    os.chmod(Test_OSXSupport.prog_name, stat.S_IRWXU)
    Test_OSXSupport.assertEqual('ExpectedOutput', _osx_support._read_output(Test_OSXSupport.prog_name))

Test_OSXSupport = test__osx_support.Test_OSXSupport()
Test_OSXSupport.setUp()
test__read_output()
