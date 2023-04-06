import genericpath
import os
import sys
import unittest
import warnings
from test.support import os_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_ok
from test.support.os_helper import FakePath
import test_genericpath

def test_expandvars():
    expandvars = CommonTest.pathmodule.expandvars
    with os_helper.EnvironmentVarGuard() as env:
        env.clear()
        env['foo'] = 'bar'
        env['{foo'] = 'baz1'
        env['{foo}'] = 'baz2'
        CommonTest.assertEqual(expandvars('foo'), 'foo')
        CommonTest.assertEqual(expandvars('$foo bar'), 'bar bar')
        CommonTest.assertEqual(expandvars('${foo}bar'), 'barbar')
        CommonTest.assertEqual(expandvars('$[foo]bar'), '$[foo]bar')
        CommonTest.assertEqual(expandvars('$bar bar'), '$bar bar')
        CommonTest.assertEqual(expandvars('$?bar'), '$?bar')
        CommonTest.assertEqual(expandvars('$foo}bar'), 'bar}bar')
        CommonTest.assertEqual(expandvars('${foo'), '${foo')
        CommonTest.assertEqual(expandvars('${{foo}}'), 'baz1}')
        CommonTest.assertEqual(expandvars('$foo$foo'), 'barbar')
        CommonTest.assertEqual(expandvars('$bar$bar'), '$bar$bar')
        CommonTest.assertEqual(expandvars(b'foo'), b'foo')
        CommonTest.assertEqual(expandvars(b'$foo bar'), b'bar bar')
        CommonTest.assertEqual(expandvars(b'${foo}bar'), b'barbar')
        CommonTest.assertEqual(expandvars(b'$[foo]bar'), b'$[foo]bar')
        CommonTest.assertEqual(expandvars(b'$bar bar'), b'$bar bar')
        CommonTest.assertEqual(expandvars(b'$?bar'), b'$?bar')
        CommonTest.assertEqual(expandvars(b'$foo}bar'), b'bar}bar')
        CommonTest.assertEqual(expandvars(b'${foo'), b'${foo')
        CommonTest.assertEqual(expandvars(b'${{foo}}'), b'baz1}')
        CommonTest.assertEqual(expandvars(b'$foo$foo'), b'barbar')
        CommonTest.assertEqual(expandvars(b'$bar$bar'), b'$bar$bar')

CommonTest = test_genericpath.CommonTest()
test_expandvars()
