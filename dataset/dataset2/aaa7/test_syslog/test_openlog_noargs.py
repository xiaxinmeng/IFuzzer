from test.support import import_helper
import unittest
import test_syslog

def test_openlog_noargs():
    test_syslog.syslog.openlog()
    test_syslog.syslog.syslog('test message from python test_syslog')

Test = test_syslog.Test()
test_openlog_noargs()
