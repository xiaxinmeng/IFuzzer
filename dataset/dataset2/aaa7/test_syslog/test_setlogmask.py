from test.support import import_helper
import unittest
import test_syslog

def test_setlogmask():
    test_syslog.syslog.setlogmask(test_syslog.syslog.LOG_DEBUG)

Test = test_syslog.Test()
test_setlogmask()
