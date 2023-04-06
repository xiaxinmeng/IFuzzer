from test.support import import_helper
import unittest
import test_syslog

def test_log_upto():
    test_syslog.syslog.LOG_UPTO(test_syslog.syslog.LOG_INFO)

Test = test_syslog.Test()
test_log_upto()
