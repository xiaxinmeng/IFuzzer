from test.support import import_helper
import unittest
import test_syslog

def test_closelog():
    test_syslog.syslog.openlog('python')
    test_syslog.syslog.closelog()

Test = test_syslog.Test()
test_closelog()
