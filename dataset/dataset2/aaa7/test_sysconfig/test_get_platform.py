import unittest
import sys
import os
import subprocess
import shutil
from copy import copy
from test.support import captured_stdout, PythonSymlink
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink, skip_unless_symlink, change_cwd
from test.support.warnings_helper import check_warnings
import sysconfig
from sysconfig import get_paths, get_platform, get_config_vars, get_path, get_path_names, _INSTALL_SCHEMES, _get_default_scheme, _expand_vars, get_scheme_names, get_config_var, _main
import _osx_support
import _imp
import platform, re
import test_sysconfig

def test_get_platform():
    os.name = 'nt'
    sys.version = '2.4.4 (#71, Oct 18 2006, 08:34:43) [MSC v.1310 32 bit (Intel)]'
    sys.platform = 'win32'
    TestSysConfig.assertEqual(get_platform(), 'win32')
    os.name = 'nt'
    sys.version = '2.4.4 (#71, Oct 18 2006, 08:34:43) [MSC v.1310 32 bit (Amd64)]'
    sys.platform = 'win32'
    TestSysConfig.assertEqual(get_platform(), 'win-amd64')
    os.name = 'posix'
    sys.version = '2.5 (r25:51918, Sep 19 2006, 08:49:13) \n[GCC 4.0.1 (Apple Computer, Inc. build 5341)]'
    sys.platform = 'darwin'
    TestSysConfig._set_uname(('Darwin', 'macziade', '8.11.1', 'Darwin Kernel Version 8.11.1: Wed Oct 10 18:23:28 PDT 2007; root:xnu-792.25.20~1/RELEASE_I386', 'PowerPC'))
    _osx_support._remove_original_values(get_config_vars())
    get_config_vars()['MACOSX_DEPLOYMENT_TARGET'] = '10.3'
    get_config_vars()['CFLAGS'] = '-fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes'
    maxint = sys.maxsize
    try:
        sys.maxsize = 2147483647
        TestSysConfig.assertEqual(get_platform(), 'macosx-10.3-ppc')
        sys.maxsize = 9223372036854775807
        TestSysConfig.assertEqual(get_platform(), 'macosx-10.3-ppc64')
    finally:
        sys.maxsize = maxint
    TestSysConfig._set_uname(('Darwin', 'macziade', '8.11.1', 'Darwin Kernel Version 8.11.1: Wed Oct 10 18:23:28 PDT 2007; root:xnu-792.25.20~1/RELEASE_I386', 'i386'))
    _osx_support._remove_original_values(get_config_vars())
    get_config_vars()['MACOSX_DEPLOYMENT_TARGET'] = '10.3'
    get_config_vars()['CFLAGS'] = '-fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes'
    maxint = sys.maxsize
    try:
        sys.maxsize = 2147483647
        TestSysConfig.assertEqual(get_platform(), 'macosx-10.3-i386')
        sys.maxsize = 9223372036854775807
        TestSysConfig.assertEqual(get_platform(), 'macosx-10.3-x86_64')
    finally:
        sys.maxsize = maxint
    _osx_support._remove_original_values(get_config_vars())
    get_config_vars()['MACOSX_DEPLOYMENT_TARGET'] = '10.4'
    get_config_vars()['CFLAGS'] = '-arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk  -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -O3'
    TestSysConfig.assertEqual(get_platform(), 'macosx-10.4-fat')
    _osx_support._remove_original_values(get_config_vars())
    get_config_vars()['CFLAGS'] = '-arch x86_64 -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk  -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -O3'
    TestSysConfig.assertEqual(get_platform(), 'macosx-10.4-intel')
    _osx_support._remove_original_values(get_config_vars())
    get_config_vars()['CFLAGS'] = '-arch x86_64 -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk  -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -O3'
    TestSysConfig.assertEqual(get_platform(), 'macosx-10.4-fat3')
    _osx_support._remove_original_values(get_config_vars())
    get_config_vars()['CFLAGS'] = '-arch ppc64 -arch x86_64 -arch ppc -arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk  -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -O3'
    TestSysConfig.assertEqual(get_platform(), 'macosx-10.4-universal')
    _osx_support._remove_original_values(get_config_vars())
    get_config_vars()['CFLAGS'] = '-arch x86_64 -arch ppc64 -isysroot /Developer/SDKs/MacOSX10.4u.sdk  -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -O3'
    TestSysConfig.assertEqual(get_platform(), 'macosx-10.4-fat64')
    for arch in ('ppc', 'i386', 'x86_64', 'ppc64'):
        _osx_support._remove_original_values(get_config_vars())
        get_config_vars()['CFLAGS'] = '-arch %s -isysroot /Developer/SDKs/MacOSX10.4u.sdk  -fno-strict-aliasing -fno-common -dynamic -DNDEBUG -g -O3' % arch
        TestSysConfig.assertEqual(get_platform(), 'macosx-10.4-%s' % arch)
    os.name = 'posix'
    sys.version = '2.3.5 (#1, Jul  4 2007, 17:28:59) \n[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)]'
    sys.platform = 'linux2'
    TestSysConfig._set_uname(('Linux', 'aglae', '2.6.21.1dedibox-r7', '#1 Mon Apr 30 17:25:38 CEST 2007', 'i686'))
    TestSysConfig.assertEqual(get_platform(), 'linux-i686')

TestSysConfig = test_sysconfig.TestSysConfig()
test_get_platform()
