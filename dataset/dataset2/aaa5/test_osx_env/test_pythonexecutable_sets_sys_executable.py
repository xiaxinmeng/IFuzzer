from test.support.os_helper import EnvironmentVarGuard
import subprocess
import sys
import sysconfig
import unittest
import test_osx_env

def test_pythonexecutable_sets_sys_executable():
    OSXEnvironmentVariableTestCase._check_sys('PYTHONEXECUTABLE', '==', 'sys.executable')

OSXEnvironmentVariableTestCase = test_osx_env.OSXEnvironmentVariableTestCase()
test_pythonexecutable_sets_sys_executable()
