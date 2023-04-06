from test.support import import_helper
import unittest
import test_syslog

def test_openlog():
    test_syslog.syslog.openlog('python')
    Test.assertRaises(UnicodeEncodeError, test_syslog.syslog.openlog, '\ud800')

Test = test_syslog.Test()
test_openlog()
